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
            ret = obj.getparams()
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        W_T1 = 0
        while (W_T1 in range(0, 1)):
            W_T1 += 1
            with open('/dev/null', 'r'):
                W_O1 = 0
                while (W_O1 in range(0, 1)):
                    W_O1 += 1
                    if True:
                        dc = demoCls()
                        dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
