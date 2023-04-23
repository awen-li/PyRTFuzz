from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_read(None)
        ret = obj.getcompname()
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    for F_h1 in range(0, 1):
        if True:
            with open('/dev/null', 'r'):
                W_V1 = 0
                while (W_V1 in range(0, 1)):
                    W_V1 += 1
                    if True:
                        PyCall_1682118013_ccgOa(x)

def PyCall_1682118013_ccgOa(x):
    for F_R1 in range(0, 1):
        if True:
            demoFunc(x)
