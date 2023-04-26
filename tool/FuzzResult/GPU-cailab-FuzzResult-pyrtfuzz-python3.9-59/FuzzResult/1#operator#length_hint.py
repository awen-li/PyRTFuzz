from fuzzwrap import PyDecode 
from operator import *
import operator

API_TYPE_LIST = ['list', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (obj, default) = PyDecode(API_TYPE_LIST, arg)
            ret = operator.length_hint(obj, default)
        except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
