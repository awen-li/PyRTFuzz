from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['_sunau_params']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_write(None)
            params = PyDecode(API_TYPE_LIST, arg)
            obj.setparams(params)
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682445561_FiSUd(x)

def PyCall_1682445561_alGAi(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682445561_PFbWE(x):
    if True:
        with open('/dev/null', 'r'):
            if True:
                with open('/dev/null', 'r'):
                    PyCall_1682445561_alGAi(x)

def PyCall_1682445561_FiSUd(x):
    with open('/dev/null', 'r'):
        if True:
            PyCall_1682445561_PFbWE(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
