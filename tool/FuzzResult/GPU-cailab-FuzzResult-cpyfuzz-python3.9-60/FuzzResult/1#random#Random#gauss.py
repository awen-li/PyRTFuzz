from fuzzwrap import PyDecode 
from random import *
import random
from math import e

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int', 'int']

def demoFunc(arg):
    try:
        obj = random.Random()
        (mu, sigma) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.gauss(mu, sigma)
        repr(obj)
    except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
