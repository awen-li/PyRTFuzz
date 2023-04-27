from fuzzwrap import PyDecode 
from random import *
import random
from math import e

CLS_TYPE_LIST = ['None']
API_TYPE_LIST = ['float', 'float']

def demoFunc(arg):
    try:
        obj = random.Random()
        (alpha, beta) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.weibullvariate(alpha, beta)
        repr(obj)
    except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682336282_wIxZx(x)

def PyCall_1682336282_wIxZx(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                for F_A1 in range(0, 1):
                    if True:
                        demoFunc(x)
