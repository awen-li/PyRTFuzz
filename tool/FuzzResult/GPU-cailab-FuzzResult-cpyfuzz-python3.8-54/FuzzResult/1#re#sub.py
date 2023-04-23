from fuzzwrap import PyDecode 
from re import *
import re
import sre_parse

API_TYPE_LIST = ['str', 'str', 'str', 'int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (pattern, repl, string, count, flags) = PyDecode(API_TYPE_LIST, arg)
            ret = re.sub(pattern, repl, string, count, flags)
        except (AssertionError, AttributeError, ImportError, KeyError, LookupError, OSError, RuntimeError, StopIteration, TypeError, ValueError, sre_parse.Verbose) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
