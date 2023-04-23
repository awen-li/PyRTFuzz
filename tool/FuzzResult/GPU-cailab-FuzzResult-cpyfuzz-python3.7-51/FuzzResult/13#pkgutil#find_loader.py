from fuzzwrap import PyDecode 
from pkgutil import *
import pkgutil

API_TYPE_LIST = ['str']

def demoFunc(arg):
    try:
        fullname = PyDecode(API_TYPE_LIST, arg)
        ret = pkgutil.find_loader(fullname)
    except (AssertionError, AttributeError, Exception, ImportError, KeyError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682152939_RtnEr(x)

def PyCall_1682152939_bYSjw(x):
    if True:
        demoFunc(x)

def PyCall_1682152939_CFdHl(x):
    PyCall_1682152939_bYSjw(x)

def PyCall_1682152939_jNIxF(x):
    PyCall_1682152939_CFdHl(x)

def PyCall_1682152939_RtnEr(x):
    PyCall_1682152939_jNIxF(x)
