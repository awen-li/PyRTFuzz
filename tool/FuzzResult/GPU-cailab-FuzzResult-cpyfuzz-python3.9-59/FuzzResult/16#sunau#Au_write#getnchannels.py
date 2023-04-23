from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_write(None)
        ret = obj.getnchannels()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        W_k1 = 0
        while (W_k1 in range(0, 1)):
            W_k1 += 1
            PyCall_1682266680_IaXjB(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682266680_xEIbj(x):
    for F_z1 in range(0, 1):
        for F_T1 in range(0, 1):
            demoFunc(x)

def PyCall_1682266680_VyynB(x):
    PyCall_1682266680_xEIbj(x)

def PyCall_1682266680_NkTUZ(x):
    PyCall_1682266680_VyynB(x)

def PyCall_1682266680_IaXjB(x):
    if True:
        with open('/dev/null', 'r'):
            if True:
                if True:
                    PyCall_1682266680_NkTUZ(x)
