from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        ret = obj.getsampwidth()
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682130005_ObOul(x)

def PyCall_1682130005_sRlMc(x):
    with open('/dev/null', 'r'):
        if True:
            demoFunc(x)

def PyCall_1682130005_kEqBL(x):
    PyCall_1682130005_sRlMc(x)

def PyCall_1682130005_ObOul(x):
    PyCall_1682130005_kEqBL(x)
