from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = sunau.Au_read(None)
        ret = obj.getcomptype()
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682117283_tcGMR(x)

def PyCall_1682117283_LwUlo(x):
    if True:
        demoFunc(x)

def PyCall_1682117283_zeXmx(x):
    if True:
        with open('/dev/null', 'r'):
            PyCall_1682117283_LwUlo(x)

def PyCall_1682117283_rfVeB(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682117283_zeXmx(x)

def PyCall_1682117283_tcGMR(x):
    PyCall_1682117283_rfVeB(x)
