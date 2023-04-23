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
            ret = obj.getnframes()
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        W_E1 = 0
        while (W_E1 in range(0, 1)):
            W_E1 += 1
            if True:
                PyCall_1682099669_fOGzh(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682099669_fOGzh(x):
    if True:
        with open('/dev/null', 'r'):
            for F_p1 in range(0, 1):
                dc = demoCls()
                dc.demoFunc(x)
