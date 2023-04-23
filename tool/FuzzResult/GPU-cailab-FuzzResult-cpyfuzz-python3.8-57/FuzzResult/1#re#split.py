from fuzzwrap import PyDecode 
from re import *
import re
import sre_parse

API_TYPE_LIST = ['str', 'str', 'int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (pattern, string, maxsplit, flags) = PyDecode(API_TYPE_LIST, arg)
            ret = re.split(pattern, string, maxsplit, flags)
        except (AssertionError, AttributeError, ImportError, KeyError, LookupError, OSError, RuntimeError, StopIteration, TypeError, ValueError, sre_parse.Verbose) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
