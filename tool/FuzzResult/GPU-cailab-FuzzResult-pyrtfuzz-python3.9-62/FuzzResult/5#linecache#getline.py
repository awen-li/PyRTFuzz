from fuzzwrap import PyDecode 
from linecache import *
import linecache
import tokenize

API_TYPE_LIST = ['str', 'int', 'dict']

def demoFunc(arg):
    try:
        (filename, lineno, module_globals) = PyDecode(API_TYPE_LIST, arg)
        ret = linecache.getline(filename, lineno, module_globals)
    except (AssertionError, AttributeError, LookupError, MemoryError, OSError, TypeError, ValueError, tokenize.StopTokenizing, tokenize.TokenError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682396389_iaMJF(x)

def PyCall_1682396389_iaMJF(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
