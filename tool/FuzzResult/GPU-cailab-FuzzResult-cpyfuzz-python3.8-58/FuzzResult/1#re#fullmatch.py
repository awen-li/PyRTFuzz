from fuzzwrap import PyDecode 
from re import *
import re
import sre_parse

API_TYPE_LIST = ['bytes', 'bytes', 'int']

def demoFunc(arg):
    try:
        (pattern, string, flags) = PyDecode(API_TYPE_LIST, arg)
        ret = re.fullmatch(pattern, string, flags)
    except (AssertionError, AttributeError, ImportError, KeyError, LookupError, OSError, RuntimeError, StopIteration, TypeError, ValueError, sre_parse.Verbose) as e:
        pass

def RunFuzzer(x):
    if True:
        demoFunc(x)
