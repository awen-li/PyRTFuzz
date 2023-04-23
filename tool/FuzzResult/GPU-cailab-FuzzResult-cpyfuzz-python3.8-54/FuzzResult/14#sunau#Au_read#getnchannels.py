from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_read(None)
            ret = obj.getnchannels()
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682234481_Raobl(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682234481_kdekZ(x):
    W_f1 = 0
    while (W_f1 in range(0, 1)):
        W_f1 += 1
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682234481_Raobl(x):
    with open('/dev/null', 'r'):
        for F_w1 in range(0, 1):
            W_N1 = 0
            while (W_N1 in range(0, 1)):
                W_N1 += 1
                for F_l1 in range(0, 1):
                    W_L1 = 0
                    while (W_L1 in range(0, 1)):
                        W_L1 += 1
                        with open('/dev/null', 'r'):
                            W_V1 = 0
                            while (W_V1 in range(0, 1)):
                                W_V1 += 1
                                PyCall_1682234481_kdekZ(x)
