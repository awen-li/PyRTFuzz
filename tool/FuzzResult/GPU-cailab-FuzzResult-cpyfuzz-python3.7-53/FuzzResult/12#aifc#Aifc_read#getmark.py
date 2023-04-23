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
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    for F_c1 in range(0, 1):
        PyCall_1682119686_PHQQL(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682119686_PHQQL(x):
    if True:
        with open('/dev/null', 'r'):
            for F_b1 in range(0, 1):
                if True:
                    with open('/dev/null', 'r'):
                        for F_u1 in range(0, 1):
                            demoFunc(x)
