from fuzzwrap import PyDecode 
from random import *
import random
from math import e

CLS_TYPE_LIST = ['None']
API_TYPE_LIST = ['float']

def demoFunc(arg):
    try:
        obj = random.Random()
        alpha = PyDecode(API_TYPE_LIST, arg)
        ret = obj.paretovariate(alpha)
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, TypeError, ValueError, ZeroDivisionError) as e:
        pass

def RunFuzzer(x):
    for F_F1 in range(0, 1):
        if True:
            PyCall_1682179791_BUmhx(x)

def PyCall_1682179791_CUqkW(x):
    for F_c1 in range(0, 1):
        demoFunc(x)

def PyCall_1682179791_lMcno(x):
    PyCall_1682179791_CUqkW(x)

def PyCall_1682179791_BUmhx(x):
    W_v1 = 0
    while (W_v1 in range(0, 1)):
        W_v1 += 1
        PyCall_1682179791_lMcno(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
