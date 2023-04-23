from fuzzwrap import PyDecode 
from pprint import *
import pprint
import re
from io import StringIO

API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        object = PyDecode(API_TYPE_LIST, arg)
        ret = pprint.isrecursive(object)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, LookupError, OSError, StopIteration, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    if True:
        W_i1 = 0
        while (W_i1 in range(0, 1)):
            W_i1 += 1
            W_D1 = 0
            while (W_D1 in range(0, 1)):
                W_D1 += 1
                with open('/dev/null', 'r'):
                    PyCall_1682228597_kFfoH(x)

def PyCall_1682228597_Zgxzl(x):
    demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682228597_kFfoH(x):
    W_f1 = 0
    while (W_f1 in range(0, 1)):
        W_f1 += 1
        with open('/dev/null', 'r'):
            W_g1 = 0
            while (W_g1 in range(0, 1)):
                W_g1 += 1
                with open('/dev/null', 'r'):
                    for F_X1 in range(0, 1):
                        with open('/dev/null', 'r'):
                            PyCall_1682228597_Zgxzl(x)
