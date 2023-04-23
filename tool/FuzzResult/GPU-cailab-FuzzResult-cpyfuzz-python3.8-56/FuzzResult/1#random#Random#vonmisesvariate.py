from fuzzwrap import PyDecode 
from random import *
import random
from math import e

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['float', 'int']

def demoFunc(arg):
    try:
        obj = random.Random()
        (mu, kappa) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.vonmisesvariate(mu, kappa)
        PyPrint(obj)
    except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
