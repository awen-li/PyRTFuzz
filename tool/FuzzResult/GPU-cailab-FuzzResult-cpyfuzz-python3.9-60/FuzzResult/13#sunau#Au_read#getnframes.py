from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_read(None)
        ret = obj.getnframes()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682266638_XFIfB(x)

def PyCall_1682266638_rHPwt(x):
    if True:
        demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682266638_ipvpN(x):
    if True:
        PyCall_1682266638_rHPwt(x)

def PyCall_1682266638_qNdul(x):
    PyCall_1682266638_ipvpN(x)

def PyCall_1682266638_Wrlou(x):
    if True:
        with open('/dev/null', 'r'):
            PyCall_1682266638_qNdul(x)

def PyCall_1682266638_XFIfB(x):
    with open('/dev/null', 'r'):
        PyCall_1682266638_Wrlou(x)
