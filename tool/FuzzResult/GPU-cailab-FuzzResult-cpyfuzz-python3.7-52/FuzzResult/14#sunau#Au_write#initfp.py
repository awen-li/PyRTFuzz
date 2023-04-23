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
    for F_q1 in range(0, 1):
        if True:
            W_J1 = 0
            while (W_J1 in range(0, 1)):
                W_J1 += 1
                for F_h1 in range(0, 1):
                    if True:
                        PyCall_1682157628_pDhcv(x)

def PyCall_1682157628_pDhcv(x):
    with open('/dev/null', 'r'):
        W_i1 = 0
        while (W_i1 in range(0, 1)):
            W_i1 += 1
            for F_r1 in range(0, 1):
                with open('/dev/null', 'r'):
                    with open('/dev/null', 'r'):
                        demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
