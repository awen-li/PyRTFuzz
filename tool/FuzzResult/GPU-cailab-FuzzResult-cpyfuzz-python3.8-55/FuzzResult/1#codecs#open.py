from fuzzwrap import PyDecode 
from codecs import *
import codecs

API_TYPE_LIST = ['str', 'str', 'str', 'str', 'int']

def demoFunc(arg):
    try:
        (filename, mode, encoding, errors, buffering) = PyDecode(API_TYPE_LIST, arg)
        ret = codecs.open(filename, mode, encoding, errors, buffering)
    except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, StopIteration, TypeError, UnicodeDecodeError, ValueError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
