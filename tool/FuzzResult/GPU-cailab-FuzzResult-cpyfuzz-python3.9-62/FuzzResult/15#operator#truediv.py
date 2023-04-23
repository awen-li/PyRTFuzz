from fuzzwrap import PyDecode 
from operator import *
import operator

API_TYPE_LIST = ['int', 'int']

def demoFunc(arg):
    try:
        (a, b) = PyDecode(API_TYPE_LIST, arg)
        ret = operator.truediv(a, b)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1681712486_Yqlqm(x)

def PyCall_1681712486_VbeAS(x):
    with open('/dev/null', 'r'):
        if True:
            if True:
                with open('/dev/null', 'r'):
                    demoFunc(x)

def PyCall_1681712486_jYTZZ(x):
    with open('/dev/null', 'r'):
        PyCall_1681712486_VbeAS(x)

def PyCall_1681712486_ZRAnM(x):
    PyCall_1681712486_jYTZZ(x)

def PyCall_1681712486_HYeUz(x):
    PyCall_1681712486_ZRAnM(x)

def PyCall_1681712486_Yqlqm(x):
    PyCall_1681712486_HYeUz(x)
