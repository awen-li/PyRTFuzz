from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['BufferedWriter']

def demoFunc(arg):
    try:
        obj = sunau.Au_write(None)
        file = PyDecode(API_TYPE_LIST, arg)
        obj.initfp(file)
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                PyCall_1682141836_SwbmT(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682141836_IQVeB(x):
    W_y1 = 0
    while (W_y1 in range(0, 1)):
        W_y1 += 1
        demoFunc(x)

def PyCall_1682141836_SwbmT(x):
    if True:
        PyCall_1682141836_IQVeB(x)
