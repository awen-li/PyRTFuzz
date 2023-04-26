from fuzzwrap import PyDecode 
from bisect import *
import bisect

API_TYPE_LIST = ['list', 'int', 'int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (a, x, lo, hi) = PyDecode(API_TYPE_LIST, arg)
            ret = bisect.bisect_left(a, x, lo, hi)
        except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681348005_jrsEv(x)

def PyCall_1681348005_jrsEv(x):
    dc = demoCls()
    dc.demoFunc(x)
