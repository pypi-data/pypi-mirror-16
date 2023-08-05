import inspect
from datetime import datetime

import numpy as np
import pandas as pd
from IPython.display import HTML,Javascript,display

"""SciUnit: A Test-Driven Framework for Validation of 
     Quantitative Scientific Models"""

class Model(object):
  """Abstract base class for sciunit models."""
  def __init__(self, name=None, **params):
    if name is None:
      name = self.__class__.__name__
    self.name = name
    self.params = params
    if params is None:
      params = {}

  name = None
  """The name of the model. Defaults to the class name."""

  description = ""
  """A description of the model."""

  params = None
  """The parameters to the model (a dictionary).
  These distinguish one model of a class from another."""

  run_args = None
  """These are the run-time arguments for the model.
  Execution of run() should make use of these arguments."""

  def describe(self):
    result = "No description available"
    if len(self.description):
      result = "%s" % self.description
    else:
      try:
        s = []
        s += [self.__doc__.strip().replace('\n','').replace('    ','')]
        result = '\n'.join(s)
      except:
        pass
    return result

  def __str__(self):
    return '%s' % self.name

  def __repr__(self):
    return str(self)


class Capability(object):
  """Abstract base class for sciunit capabilities."""
  
  @classmethod
  def check(cls, model):
    """Checks whether the provided model has this capability.

    By default, uses isinstance.
    """
    return isinstance(model, cls)

  class __metaclass__(type):
      @property
      def name(cls):
        return cls.__name__


class Test(object):
  """Abstract base class for tests."""
  def __init__(self, observation, name=None, **params):
      if name is None:
        name = self.__class__.__name__
      self.name = name
      
      if self.description is None:
        self.description = self.__class__.__doc__
      
      self.params = params
      if params is None:
        params = {}
      
      self.observation = observation
      self.validate_observation(observation)

      if self.score_type is None or not issubclass(self.score_type, Score):
        raise Error("Test %s does not specify a score type." % self.name)

  name = None
  """The name of the test. Defaults to the test class name."""

  description = None
  """A description of the test. Defaults to the docstring for the class."""

  observation = None
  """The empirical observation that the test is using."""

  params = None
  """A dictionary containing the parameters to the test."""

  score_type = None
  """A score type for this test's `judge` method to return."""

  converter = None
  """A conversion to be done on the score after it is computed."""

  def validate_observation(self, observation):
    """(Optional) Implement to validate the observation provided to the 
    constructor.

    Raises an ObservationError if invalid.
    """
    return True
  
  required_capabilities = ()
  """A sequence of capabilities that a model must have in order for the 
  test to be run. Defaults to empty."""

  def check_capabilities(self, model):
    """Checks that the capabilities required by the test are 
    implemented by `model`.

    Raises an Error if model is not a Model.
    Raises a CapabilityError if model does not have a capability.
    """
    if not isinstance(model, Model):
      raise Error("Model %s is not a sciunit.Model." % str(model))

    for c in self.required_capabilities:
      if not c.check(model):
        raise CapabilityError(model, c)

    return True

  def generate_prediction(self, model, verbose=False):
    """Generates a prediction from a model using the required capabilities.

    No default implementation.
    """
    raise NotImplementedError("Test %s does not implement generate_prediction."
       % str())

  score_type = None

  def compute_score(self, observation, prediction, verbose=False):
    """Generates a score given the observations provided in the constructor
    and the prediction generated by generate_prediction.

    Must generate a score of score_type.

    No default implementation.
    """
    try:
      # After some processing of the observation and the prediction.  
      score = self.score_type.compute(observation,prediction) 
      return score
    except:
      raise NotImplementedError(("Test %s either implements no compute_score "
                                 "method or provides no score_type with a "
                                 "compute method." % self.name))

  def _bind_score(self,score,model,observation,prediction):
      """
      Binds some useful attributes to the score.
      """
      score.model = model
      score.test = self
      score.prediction = prediction
      score.observation = observation
      score.related_data = score.related_data.copy() # Don't let scores 
                                                     # share related_data.
      score = self.bind_score(score,model,observation,prediction)
      return score

  def bind_score(self,score,model,observation,prediction):
      """
      For the user to bind additional features to the score.
      """
      return score

  def _judge(self, model, verbose=False):
      # 1.
      self.check_capabilities(model)
      # 2.
      prediction = self.generate_prediction(model, verbose=verbose)
      self.last_model = model
      # 3.
      observation = self.observation
      score = self.compute_score(observation, prediction, verbose=verbose)
      if self.converter:
        score = self.converter.convert(score)
      # 4.
      if not (isinstance(score, self.score_type) or \
              isinstance(score,NoneScore) or \
              isinstance(score,ErrorScore)):
        raise InvalidScoreError(("Score for test '%s' is not of correct type. "
                                 "The test requires type %s but %s "
                                 "was provided." % (self.name,
                                                    self.score_type.__name__,
                                                    score.__class__.__name__)))
      # 5.
      score = self._bind_score(score,model,observation,prediction)
      
      return score
  
  def judge(self, model, stop_on_error=True, deep_error=False, verbose=False):
    """Generates a score for the provided model.

    Operates as follows:
    1. Checks if the model has all the required capabilities.
    2. Calls generate_prediction to generate a prediction.
    3. Calls score_prediction to generate a score.
    4. Checks that the score is of score_type, raising an InvalidScoreError.
    5. Equips the score with metadata:
       a) A reference to the model, in attribute model.
       b) A reference to the test, in attribute test.
       c) A reference to the prediction, in attribute prediction.
       d) A reference to the observation, in attribute observation.
    6. Returns the score.

    If stop_on_error is true (default), exceptions propagate upward. If false,
    an ErrorScore is generated containing the exception.
    """

    if type(model) in (list,tuple,set): # If a collection of models is provided
      suite = TestSuite(self.name, self) # then test them using a one-test suite.  
      return suite.judge(model, stop_on_error=stop_on_error, 
                                deep_error=deep_error, verbose=verbose)

    if deep_error:
      score = self._judge(model, verbose=verbose)
    else:
      try:
        score = self._judge(model, verbose=verbose)
      except CapabilityError as e:
        score = NAScore(e)
      except Exception as e:
        score = ErrorScore(e)
    if type(score) is ErrorScore and stop_on_error:
      raise score.score # An exception.  
    return score

  def check(self, model, stop_on_error=True):
    """Like judge, but without actually running the test.
    Just returns a Score indicating whether the model can take the test or not."""
    e = None
    try:
      if self.check_capabilities(model):
        score = TBDScore(None)
      else:
        score = NAScore(None)
    except Exception as e:
      score = ErrorScore(e)
    if e and stop_on_error:
      raise e
    return score

  def describe(self):
    result = "No description available"
    if len(self.description):
      result = "%s" % self.description
    else:
      try:
        s = []
        s += [self.__doc__.strip().replace('\n','').replace('    ','')]
        if self.test.converter:
          s += [self.converter.description]
        result = '\n'.join(s)
      except:
        pass
    return result

  def __str__(self):
    return '%s' % self.name

  def __repr__(self):
    return str(self)


class TestSuite(object):
  """A collection of tests."""
  def __init__(self, name, tests, hooks=None):
    if name is None:
      raise Error("Suite name required.")
    self.name = name
    if isinstance(tests, Test):
      # turn singleton test into a sequence
      tests = (tests,)
    else:
      try:
        for test in tests:
          if not isinstance(test, Test):
            raise Error("Test suite provided an iterable containing a non-Test.")
      except TypeError:
        raise Error("Test suite was not provided a test or iterable.")
    self.tests = tests
    self.hooks = hooks

  name = None
  """The name of the test suite. Defaults to the class name."""

  description = None
  """The description of the test suite. No default."""

  tests = None
  """The sequence of tests that this suite contains."""

  def judge(self, models, stop_on_error=True, deep_error=False, verbose=False):
    """Judges the provided models against each test in the test suite.

    Returns a ScoreMatrix.
    """
    if isinstance(models, Model):
      models = (models,)
    else:
      try:
        for model in models:
          if not isinstance(model, Model):
            raise Error("Test suite's judge method provided an iterable containing a non-Model.")
      except TypeError:
        raise Error("Test suite's judge method not provided a model or iterable.""")

    sm = ScoreMatrix(self.tests, models)
    for model in models:
      for test in self.tests:
        if True:#verbose:
          print('Executing %s on %s' % (test,model))
        score = test.judge(model, stop_on_error=stop_on_error, 
                           deep_error=deep_error, verbose=verbose)
        sm.loc[model, test] = score
        if self.hooks and test in self.hooks:
          f = self.hooks[test]['f']
          if 'kwargs' in self.hooks[test]:
            kwargs = self.hooks[test]['kwargs']
          else:
            kwargs = {}
          f(test, self.tests, score, **kwargs)
    return sm

  @classmethod
  def from_observations(cls, name, tests_info):
    """Instantiate a test suite with name 'name' and information about tests
    in 'tests_info', as [(TestClass1,observation1),(TestClass2,observation2),...].
    The desired test name may appear as an optional third item in the tuple, e.g.
    (TestClass1,observation1,"my_test").  The same test class may be used multiple 
    times, e.g. [(TestClass1,observation1a),(TestClass1,observation1b),...].
    """

    tests = []
    for test_info in tests_info:
      test_class = test_info[0]
      observation = test_info[1]
      test_name = None if len(test_info)<3 else test_info[2]
      assert inspect.isclass(test_class) and issubclass(test_class, Test), \
        "First item in each tuple must be a Test class"
      if test_name is not None:
        assert type(test_name) is str, "Each test name must be a string"
      tests.append(test_class(observation,name=test_name))
    return cls(name, tests)


#
# Scores
#
class Score(object):
  """Abstract base class for scores."""
  def __init__(self, score, related_data=None):
    if related_data is None:
      related_data = { }
    self.score, self.related_data = score, related_data
    if isinstance(score,Exception):
        self.__class__ = ErrorScore # Set to error score to use its summarize().
  
  score = None
  """The score itself."""

  _description = ''
  """A description of this score, i.e. how to interpret it.
  Provided in the score definition"""

  description = ''
  """A description of this score, i.e. how to interpret it.
  For the user to set in bind_score"""

  value = None
  """A raw number arising in a test's compute_score, 
  used to determine this score."""

  related_data = None
  """Data specific to the result of a test run on a model."""

  test = None
  """The test taken. Set automatically by Test.judge."""

  model = None
  """The model judged. Set automatically by Test.judge."""

  @property
  def sort_key(self):
    """A floating point version of the score used for sorting. 
    If normalized = True, this must be in the range 0.0 to 1.0,
    where larger is better (used for sorting and coloring tables)."""
    return self.score

  @property
  def summary(self):
    """Summarize the performance of a model on a test."""
    return "=== Model %s achieved score %s on test '%s'. ===" % \
      (str(self.model), str(self), self.test)

  def summarize(self):
    if self.score is not None:
      print("%s" % self.summary)

  def _describe(self):
    result = "No description available"
    if self.score is not None:
      if len(self.description):
        result = "%s" % self.description
      else:
        try:
          s = []
          s += [self.test.score_type.__doc__.strip().\
                replace('\n','').replace('    ','')]
          if self.test.converter:
            s += [self.test.converter.description]
          s += [self._description]
          result = '\n'.join(s)
        except:
          pass
    return result

  def describe(self):
    print(self._describe())

  def raw(self):
    string = '%.4g' % self.value
    if hasattr(self.value,'magnitude'):
      string += ' %s' % str(self.value.units)[4:]
    return string

  def __str__(self):
    return '%s' % self.score

  def __repr__(self):
    return str(self)

  def __eq__(self, other):
    return self.sort_key == other.sort_key

  def __ne__(self, other):
    return self.sort_key != other.sort_key

  def __gt__(self, other):
    try:
      return self.sort_key > other.sort_key
    except TypeError:
      return 0

  def __ge__(self, other):
    try:
      return self.sort_key >= other.sort_key
    except TypeError:
      return 0

  def __lt__(self, other):
    try:
      return self.sort_key < other.sort_key
    except TypeError:
      return 0

  def __le__(self, other):
    try:
      return self.sort_key <= other.sort_key
    except TypeError:
      return 0


class ErrorScore(Score):
    """A score returned when an error occurs during testing."""
    def __init__(self, exn, related_data=None):
        super(ErrorScore,self).__init__(exn, related_data)

    @property
    def sort_key(self):
        return 0.0

    @property
    def summary(self):
      """Summarize the performance of a model on a test."""
      return "=== Model %s did not complete test %s due to error %s. ===" % \
        (str(self.model), str(self.test), str(self.score))

    def __str__(self):
        return 'Error'


class NoneScore(Score):
    """A None score.  Usually indicates that the model has not been 
    checked to see if it has the capabilities required by the test."""

    def __init__(self, score, related_data={}):
        if isinstance(score,Exception) or score is None:
            super(NoneScore,self).__init__(score, related_data=related_data)
        else:
            raise InvalidScoreError("Score must an Exception string or None.")

    @property
    def sort_key(self):
        return None

    def __str__(self):
        return 'Unknown'


class TBDScore(NoneScore):
    """A TBD (to be determined) score. Indicates that the model has capabilities 
    required by the test but has not yet taken it."""

    def __init__(self, score, related_data={}):
        super(TBDScore,self).__init__(score, related_data=related_data)

    @property
    def sort_key(self):
        return None

    def __str__(self):
        return 'TBD'

        
class NAScore(NoneScore):
    """A N/A (not applicable) score. Indicates that the model doesn't have the 
    capabilities that the test requires."""

    def __init__(self, score, related_data={}):
        super(NAScore,self).__init__(score, related_data=related_data)

    @property
    def sort_key(self):
        return None


    def __str__(self):
        return 'N/A'


class ScoreArray(pd.Series):
  """
  Represents an array of scores derived from a test suite.
  Extends the pandas Series such that items are either
  models subject to a test or tests taken by a model.  
  Also displays and compute score summaries in sciunit-specific ways.  

  Can use like this, assuming n tests and m models:

    >>> sm[test]
    
    >>> sm[test]
    (score_1, ..., score_m)
    >>> sm[model]
    (score_1, ..., score_n)
  """

  def __init__(self, tests_or_models, scores=None):
    if scores is None:
      scores = [NoneScore for tom in tests_or_models]
    assert all([isinstance(tom,Test) for tom in tests_or_models]) or \
           all([isinstance(tom,Model) for tom in tests_or_models]), \
           "A ScoreArray may be indexed by only test or models"
    super(ScoreArray,self).__init__(data=scores, index=tests_or_models)
    self.index_type = 'tests' if isinstance(tests_or_models[0],Test) \
                      else 'models'
    setattr(self,self.index_type,tests_or_models)

  def __getattr__(self, name):
    if name in ['score','sort_key','related_data']:
      return self.apply(lambda x: getattr(x,name))
    else:
      return super(ScoreArray,self).__getattr__(name)
   
  def mean(self):
    """Computes a total score for each model over all the tests, 
    using the sort_key, since otherwise direct comparison across different
    kinds of scores would not be possible."""

    return self.sort_key.mean()

  def rank(self, test, model):
    """Computes the relative rank of a model on a test compared to other models 
    that were asked to take the test."""

    vals = sorted(self.sort_keys)
    rank = 1 + vals.index(self[test,model].sort_key)
    return rank

  def view(self):
    return self


class ScoreMatrix(pd.DataFrame):
  """
  Represents a matrix of scores derived from a test suite.
  Extends the pandas DataFrame such that tests are columns and models
  are the index.  
  Also displays and compute score summaries in sciunit-specific ways.  

  Can use like this, assuming n tests and m models:

    >>> sm[test]
    
    >>> sm[test]
    (score_1, ..., score_m)
    >>> sm[model]
    (score_1, ..., score_n)
  """

  def __init__(self, tests, models, scores=None):
    if scores is None:
      scores = [[NoneScore for test in tests] for model in models]
    super(ScoreMatrix,self).__init__(data=scores, index=models, columns=tests)
    self.tests = tests
    self.models = models

  show_mean = False
  sortable = False

  def __getitem__(self, item):
    if isinstance(item, Test):
      return ScoreArray(self.models, 
                        scores=super(ScoreMatrix,self).__getitem__(item))
    elif isinstance(item, Model):
      return ScoreArray(self.tests, scores=self.loc[item,:])
    elif type(item) in (list,tuple) and len(item)==2:
      if isinstance(item[0], Test) and isinstance(item[1], Model):
        return self.loc[item[1],item[0]]
      elif isinstance(item[1], Test) and isinstance(item[0], Model):
        return self.loc[item[0],item[1]]
    raise TypeError("Expected test; model; test,model; or model,test")
  
  def __getattr__(self, name):
    if name in ['score','sort_key','related_data']:
      return self.applymap(lambda x: getattr(x,name))
    else:
      return super(ScoreMatrix,self).__getattr__(name)
       
  def rank(self, test, model):
    """Computes the relative rank of a model on a test compared to other models 
    that were asked to take the test."""

    vals = sorted([x.sort_key for x in self[model].scores])
    rank = 1 + vals.index(self[test,model].sort_key)
    return rank

  def to_html(self, show_mean=None, sortable=None, colorize=True, *args, 
              **kwargs):
    if show_mean is None:
      show_mean = self.show_mean
    if sortable is None:
      sortable = self.sortable
    df = self.copy()
    if show_mean:
      df.insert(0,'Mean',None)
      df.loc[:,'Mean'] = ['%.3f' % self[m].mean() for m in self.models]
    html = df.to_html(*args, **kwargs) # Pandas method
    import bs4
    soup = bs4.BeautifulSoup(html)
    if colorize: 
      for i,row in enumerate(soup.find('thead').findAll('tr')):
        for j,cell in enumerate(row.findAll('th')[1:]):
          if show_mean and j==0:
            value = float(df.loc[self.models[i],'Mean'])
            cell['title'] = 'Mean sort key value across tests'
          else:
            j_ = j-bool(show_mean)
            test = self.tests[j_]
            cell['title'] = test.description
            # Remove ' test' from column headers
            if cell.string[-5:] == ' test':
              cell.string = cell.string[:-5]
      for i,row in enumerate(soup.find('tbody').findAll('tr')):
        cell = row.find('th')
        cell['title'] = self.models[i].describe()
        for j,cell in enumerate(row.findAll('td')):
          if show_mean and j==0:
            value = float(df.loc[self.models[i],'Mean'])
            cell['title'] = 'Mean sort key value across tests'
          else:
            j_ = j-bool(show_mean)
            score = self[self.models[i],self.tests[j_]]
            value = score.sort_key
            cell['title'] = score._describe()
          if value is not None and not np.isnan(value):
            rgb = (255,int(255 * value),int(255 * value))
          else:
            rgb = (128,128,128)
          cell['style'] = 'background-color: rgb(%d,%d,%d);' % rgb

    table = soup.find('table')
    table_id = table['id'] = hash(datetime.now())
    html = str(soup)
    if sortable:
      js = Javascript("$('#%s').dataTable();" % table_id,
        lib=["//ajax.aspnetcdn.com/ajax/jquery.dataTables/1.9.0/jquery.dataTables.min.js"],
        css=["//ajax.aspnetcdn.com/ajax/jquery.dataTables/1.9.0/css/jquery.dataTables.css"])
      display(js)
    return html
    
  def view(self, *args, **kwargs):
    html = self.to_html(*args, **kwargs)
    return HTML(html)


class ScorePanel(pd.Panel):
  def __getitem__(self,item):
    df = super(ScorePanel,self).__getitem__(item)
    assert isinstance(df,pd.DataFrame), \
      "Only Score Matrices can be accessed by attribute from Score Panels"
    score_matrix = ScoreMatrix(models=df.index, tests=df.columns, scores=df)
    return score_matrix 


class Error(Exception):
  """Base class for errors in sciunit's core."""


class ObservationError(Error):
  """Raised when an observation passed to a test is invalid."""
  pass


class CapabilityError(Exception):
  """Error raised when a required capability is not 
  provided by a model."""
  def __init__(self, model, capability):
    self.model = model
    self.capability = capability

    super(CapabilityError,self).__init__(\
      "Model %s does not provide required capability: %s" % \
      (model.name,capability.__name__))
  
  model = None
  """The model that does not have the capability."""

  capability = None
  """The capability that is not provided."""


class InvalidScoreError(Exception):
  """Error raised when a score is invalid."""
