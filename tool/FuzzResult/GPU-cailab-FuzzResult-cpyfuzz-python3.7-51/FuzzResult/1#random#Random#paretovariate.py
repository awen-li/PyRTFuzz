from fuzzwrap import PyDecode 
from random import *
import random
from math import e

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['float']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = random.Random()
            alpha = PyDecode(API_TYPE_LIST, arg)
            ret = obj.paretovariate(alpha)
            PyPrint(obj)
        except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
