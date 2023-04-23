from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['bytes']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_write(None)
            data = PyDecode(API_TYPE_LIST, arg)
            obj.writeframes(data)
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682143397_rjacZ(x)

def PyCall_1682143397_ZCrKj(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyCall_1682143397_RSkUS(x):
    with open('/dev/null', 'r'):
        if True:
            W_S1 = 0
            while (W_S1 in range(0, 1)):
                W_S1 += 1
                for F_s1 in range(0, 1):
                    for F_u1 in range(0, 1):
                        PyCall_1682143397_ZCrKj(x)

def PyCall_1682143397_yusjP(x):
    for F_R1 in range(0, 1):
        PyCall_1682143397_RSkUS(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682143397_rjacZ(x):
    W_z1 = 0
    while (W_z1 in range(0, 1)):
        W_z1 += 1
        if True:
            PyCall_1682143397_yusjP(x)
