from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['BufferedWriter']

def demoFunc(arg):
    try:
        obj = aifc.Aifc_write(None)
        file = PyDecode(API_TYPE_LIST, arg)
        obj.initfp(file)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            PyCall_1682193024_DrjqL(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682193024_SWoUj(x):
    demoFunc(x)

def PyCall_1682193024_DrjqL(x):
    if True:
        with open('/dev/null', 'r'):
            PyCall_1682193024_SWoUj(x)
