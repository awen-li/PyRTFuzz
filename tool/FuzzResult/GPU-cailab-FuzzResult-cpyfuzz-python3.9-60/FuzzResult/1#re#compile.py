from fuzzwrap import PyDecode 
from re import *
import re
import sre_parse

API_TYPE_LIST = ['str', 'RegexFlag']

def demoFunc(arg):
    try:
        (pattern, flags) = PyDecode(API_TYPE_LIST, arg)
        ret = re.compile(pattern, flags)
    except (AssertionError, AttributeError, ImportError, KeyError, LookupError, OSError, RuntimeError, StopIteration, TypeError, ValueError, sre_parse.Verbose) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
