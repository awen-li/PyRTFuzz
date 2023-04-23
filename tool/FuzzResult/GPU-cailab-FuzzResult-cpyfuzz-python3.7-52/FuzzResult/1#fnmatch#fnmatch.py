from fuzzwrap import PyDecode 
from fnmatch import *
import fnmatch
import re

API_TYPE_LIST = ['str', 'str']

def demoFunc(arg):
    try:
        (name, pat) = PyDecode(API_TYPE_LIST, arg)
        ret = fnmatch.fnmatch(name, pat)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681356750_mxJFg(x)

def PyCall_1681356750_mxJFg(x):
    demoFunc(x)
