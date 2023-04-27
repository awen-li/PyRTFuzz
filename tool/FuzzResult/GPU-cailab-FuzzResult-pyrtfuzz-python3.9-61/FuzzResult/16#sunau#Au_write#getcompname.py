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
            obj = sunau.Au_write(None)
            ret = obj.getcompname()
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        W_h1 = 0
        while (W_h1 in range(0, 1)):
            W_h1 += 1
            for F_d1 in range(0, 1):
                W_H1 = 0
                while (W_H1 in range(0, 1)):
                    W_H1 += 1
                    W_E1 = 0
                    while (W_E1 in range(0, 1)):
                        W_E1 += 1
                        W_X1 = 0
                        while (W_X1 in range(0, 1)):
                            W_X1 += 1
                            if True:
                                PyCall_1682297277_xtxfe(x)

def PyCall_1682297277_xtxfe(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
