from fuzzwrap import PyDecode 
from operator import *
import operator

API_TYPE_LIST = ['list', 'int']

def demoFunc(arg):
    try:
        (obj, default) = PyDecode(API_TYPE_LIST, arg)
        ret = operator.length_hint(obj, default)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681352792_VPQFV(x)

def PyCall_1681352792_VPQFV(x):
    demoFunc(x)
