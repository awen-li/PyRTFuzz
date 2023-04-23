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
            ret = obj.getsampwidth()
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682163413_xDWDB(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682163413_xDWDB(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                for F_M1 in range(0, 1):
                    with open('/dev/null', 'r'):
                        for F_m1 in range(0, 1):
                            with open('/dev/null', 'r'):
                                if True:
                                    dc = demoCls()
                                    dc.demoFunc(x)
