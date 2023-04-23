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
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, LookupError, NotImplementedError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
            pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            if True:
                with open('/dev/null', 'r'):
                    PyCall_1682135024_bdhUV(x)

def PyCall_1682135024_xaiKq(x):
    if True:
        if True:
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682135024_VXURc(x):
    with open('/dev/null', 'r'):
        PyCall_1682135024_xaiKq(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682135024_bdhUV(x):
    PyCall_1682135024_VXURc(x)
