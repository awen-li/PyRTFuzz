from fuzzwrap import PyDecode 
from re import *
import re
import sre_parse

API_TYPE_LIST = ['str', 'str', 'str', 'int', 'int']

def demoFunc(arg):
    try:
        (pattern, repl, string, count, flags) = PyDecode(API_TYPE_LIST, arg)
        ret = re.subn(pattern, repl, string, count, flags)
    except (AssertionError, AttributeError, ImportError, KeyError, LookupError, OSError, RuntimeError, StopIteration, TypeError, ValueError, sre_parse.Verbose) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
