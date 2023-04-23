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
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        PyCall_1682120559_nBkTf(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682120559_nBkTf(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                if True:
                    dc = demoCls()
                    dc.demoFunc(x)
