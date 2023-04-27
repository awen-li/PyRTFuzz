from fuzzwrap import PyDecode 
from sre_compile import *
import sre_compile
import sre_parse

API_TYPE_LIST = ['str', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (p, flags) = PyDecode(API_TYPE_LIST, arg)
            ret = sre_compile.compile(p, flags)
        except (AssertionError, AttributeError, IndexError, LookupError, OSError, TypeError, ValueError, sre_parse.Verbose) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
