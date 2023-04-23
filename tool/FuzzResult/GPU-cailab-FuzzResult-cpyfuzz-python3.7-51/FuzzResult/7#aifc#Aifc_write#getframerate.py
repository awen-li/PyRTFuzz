from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_write(None)
        ret = obj.getframerate()
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682173945_agFtC(x)

def PyCall_1682173945_agFtC(x):
    with open('/dev/null', 'r'):
        if True:
            with open('/dev/null', 'r'):
                if True:
                    demoFunc(x)
