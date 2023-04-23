from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_read(None)
        ret = obj.getfp()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        PyCall_1682141953_DusPx(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682141953_GbliE(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            if True:
                with open('/dev/null', 'r'):
                    demoFunc(x)

def PyCall_1682141953_DusPx(x):
    if True:
        PyCall_1682141953_GbliE(x)
