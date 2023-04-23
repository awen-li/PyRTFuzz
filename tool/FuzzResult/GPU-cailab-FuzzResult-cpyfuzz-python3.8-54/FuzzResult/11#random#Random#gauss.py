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
        PyPrint(obj)
    except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
        pass

def RunFuzzer(x):
    PyCall_1682203507_DXZFk(x)

def PyCall_1682203507_msNmS(x):
    demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682203507_DXZFk(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                if True:
                    with open('/dev/null', 'r'):
                        if True:
                            PyCall_1682203507_msNmS(x)
