from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

API_TYPE_LIST = ['BytesIO', 'str']

def demoFunc(arg):
    try:
        (f, mode) = PyDecode(API_TYPE_LIST, arg)
        ret = aifc.open(f, mode)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682111204_nrvob(x)

def PyCall_1682111204_JyXdD(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            if True:
                demoFunc(x)

def PyCall_1682111204_uDPuX(x):
    PyCall_1682111204_JyXdD(x)

def PyCall_1682111204_nrvob(x):
    PyCall_1682111204_uDPuX(x)
