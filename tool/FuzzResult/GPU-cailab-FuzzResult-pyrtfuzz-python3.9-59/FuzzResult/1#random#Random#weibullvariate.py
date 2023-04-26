from fuzzwrap import PyDecode 
from random import *
import random
from math import e

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['float', 'float']

def demoFunc(arg):
    try:
        obj = random.Random()
        (alpha, beta) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.weibullvariate(alpha, beta)
    except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        demoFunc(x)
