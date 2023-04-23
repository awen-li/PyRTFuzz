from fuzzwrap import PyDecode 
from sunau import *
import sunau

API_TYPE_LIST = ['str', 'str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (f, mode) = PyDecode(API_TYPE_LIST, arg)
            ret = sunau.openfp(f, mode)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    W_Y1 = 0
    while (W_Y1 in range(0, 1)):
        W_Y1 += 1
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                if True:
                    W_e1 = 0
                    while (W_e1 in range(0, 1)):
                        W_e1 += 1
                        if True:
                            PyCall_1682111226_ywtWw(x)

def PyCall_1682111226_fRFCX(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyCall_1682111226_ywtWw(x):
    with open('/dev/null', 'r'):
        W_T1 = 0
        while (W_T1 in range(0, 1)):
            W_T1 += 1
            if True:
                PyCall_1682111226_fRFCX(x)
