from fuzzwrap import PyDecode 
from operator import *
import operator

API_TYPE_LIST = ['int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (a, b) = PyDecode(API_TYPE_LIST, arg)
            ret = operator.truediv(a, b)
        except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
