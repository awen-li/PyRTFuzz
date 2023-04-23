from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['_sunau_params']

def demoFunc(arg):
    try:
        obj = sunau.Au_write(None)
        params = PyDecode(API_TYPE_LIST, arg)
        obj.setparams(params)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            PyCall_1682107892_MacZZ(x)

def PyCall_1682107892_MacZZ(x):
    W_R1 = 0
    while (W_R1 in range(0, 1)):
        W_R1 += 1
        if True:
            with open('/dev/null', 'r'):
                W_g1 = 0
                while (W_g1 in range(0, 1)):
                    W_g1 += 1
                    demoFunc(x)
