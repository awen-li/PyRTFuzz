from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_read(None)
        ret = obj.getsampwidth()
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682208779_eewmU(x)

def PyCall_1682208779_rhdDM(x):
    W_Y1 = 0
    while (W_Y1 in range(0, 1)):
        W_Y1 += 1
        demoFunc(x)

def PyCall_1682208779_eewmU(x):
    with open('/dev/null', 'r'):
        W_Y1 = 0
        while (W_Y1 in range(0, 1)):
            W_Y1 += 1
            with open('/dev/null', 'r'):
                for F_K1 in range(0, 1):
                    PyCall_1682208779_rhdDM(x)
