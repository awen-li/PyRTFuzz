from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_write(None)
        ret = obj.getcompname()
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        PyCall_1682165857_RhTTJ(x)

def PyCall_1682165857_OJKVE(x):
    demoFunc(x)

def PyCall_1682165857_lBqnL(x):
    PyCall_1682165857_OJKVE(x)

def PyCall_1682165857_IwUTa(x):
    if True:
        PyCall_1682165857_lBqnL(x)

def PyCall_1682165857_RhTTJ(x):
    with open('/dev/null', 'r'):
        PyCall_1682165857_IwUTa(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
