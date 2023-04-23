from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        ret = obj.getcomptype()
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682209012_arZkj(x)

def PyCall_1682209012_arZkj(x):
    demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
