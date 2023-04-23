from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_write(None)
        ret = obj.getcomptype()
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682160233_fFRfu(x)

def PyCall_1682160233_lgCai(x):
    demoFunc(x)

def PyCall_1682160233_fFRfu(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                PyCall_1682160233_lgCai(x)
