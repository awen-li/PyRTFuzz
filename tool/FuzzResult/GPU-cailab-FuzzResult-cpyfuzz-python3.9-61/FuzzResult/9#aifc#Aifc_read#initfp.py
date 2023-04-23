from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['BufferedReader']

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        file = PyDecode(API_TYPE_LIST, arg)
        obj.initfp(file)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682175790_KGCUd(x)

def PyCall_1682175790_RJuaK(x):
    if True:
        with open('/dev/null', 'r'):
            demoFunc(x)

def PyCall_1682175790_bOGmQ(x):
    with open('/dev/null', 'r'):
        PyCall_1682175790_RJuaK(x)

def PyCall_1682175790_ZSxWE(x):
    PyCall_1682175790_bOGmQ(x)

def PyCall_1682175790_KGCUd(x):
    PyCall_1682175790_ZSxWE(x)
