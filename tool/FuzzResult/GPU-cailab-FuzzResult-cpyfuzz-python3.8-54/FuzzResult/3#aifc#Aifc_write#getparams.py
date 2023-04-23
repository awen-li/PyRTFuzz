from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_write(None)
        ret = obj.getparams()
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682189280_bLyvu(x)

def PyCall_1682189280_HYFQb(x):
    demoFunc(x)

def PyCall_1682189280_bLyvu(x):
    with open('/dev/null', 'r'):
        PyCall_1682189280_HYFQb(x)
