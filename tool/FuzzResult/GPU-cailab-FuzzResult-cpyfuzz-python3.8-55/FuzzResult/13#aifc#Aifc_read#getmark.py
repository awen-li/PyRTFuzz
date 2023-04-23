from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        id = PyDecode(API_TYPE_LIST, arg)
        ret = obj.getmark(id)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682195634_JVAAf(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682195634_NUbne(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            if True:
                demoFunc(x)

def PyCall_1682195634_MsBsX(x):
    if True:
        PyCall_1682195634_NUbne(x)

def PyCall_1682195634_JVAAf(x):
    with open('/dev/null', 'r'):
        PyCall_1682195634_MsBsX(x)
