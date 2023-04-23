from fuzzwrap import PyDecode 
from fnmatch import *
import fnmatch
import re

API_TYPE_LIST = ['generator', 'str']

def demoFunc(arg):
    try:
        (names, pat) = PyDecode(API_TYPE_LIST, arg)
        ret = fnmatch.filter(names, pat)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
