from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_write(None)
        ret = obj.getcomptype()
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        W_p1 = 0
        while (W_p1 in range(0, 1)):
            W_p1 += 1
            if True:
                W_E1 = 0
                while (W_E1 in range(0, 1)):
                    W_E1 += 1
                    with open('/dev/null', 'r'):
                        PyCall_1682207150_frfJe(x)

def PyCall_1682207150_TwoVo(x):
    with open('/dev/null', 'r'):
        W_V1 = 0
        while (W_V1 in range(0, 1)):
            W_V1 += 1
            with open('/dev/null', 'r'):
                W_G1 = 0
                while (W_G1 in range(0, 1)):
                    W_G1 += 1
                    demoFunc(x)

def PyCall_1682207150_frfJe(x):
    if True:
        PyCall_1682207150_TwoVo(x)
