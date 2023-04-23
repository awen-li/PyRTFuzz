from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        obj = aifc.Aifc_write(None)
        id = PyDecode(API_TYPE_LIST, arg)
        ret = obj.getmark(id)
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            if True:
                if True:
                    with open('/dev/null', 'r'):
                        PyCall_1682118675_kNirS(x)

def PyCall_1682118675_kNirS(x):
    demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
