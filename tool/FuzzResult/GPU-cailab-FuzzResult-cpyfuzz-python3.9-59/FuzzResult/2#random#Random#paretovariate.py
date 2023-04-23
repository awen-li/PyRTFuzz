from fuzzwrap import PyDecode 
from random import *
import random
from math import e

CLS_TYPE_LIST = ['None']
API_TYPE_LIST = ['float']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = random.Random()
            alpha = PyDecode(API_TYPE_LIST, arg)
            ret = obj.paretovariate(alpha)
            repr(obj)
        except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
            pass

def RunFuzzer(x):
    for F_x1 in range(0, 1):
        dc = demoCls()
        dc.demoFunc(x)
