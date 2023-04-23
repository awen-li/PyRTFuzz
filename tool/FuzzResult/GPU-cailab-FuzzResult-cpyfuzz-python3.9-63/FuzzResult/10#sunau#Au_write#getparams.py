from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_write(None)
        ret = obj.getparams()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    W_Q1 = 0
    while (W_Q1 in range(0, 1)):
        W_Q1 += 1
        PyCall_1682151294_NGOfq(x)

def PyCall_1682151294_ebEzH(x):
    with open('/dev/null', 'r'):
        demoFunc(x)

def PyCall_1682151294_NGOfq(x):
    PyCall_1682151294_ebEzH(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
