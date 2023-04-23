from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['bytes']

def demoFunc(arg):
    try:
        obj = aifc.Aifc_write(None)
        data = PyDecode(API_TYPE_LIST, arg)
        obj.writeframes(data)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682142677_bIHYG(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682142677_JjnEj(x):
    for F_y1 in range(0, 1):
        W_G1 = 0
        while (W_G1 in range(0, 1)):
            W_G1 += 1
            demoFunc(x)

def PyCall_1682142677_JZrNJ(x):
    for F_k1 in range(0, 1):
        PyCall_1682142677_JjnEj(x)

def PyCall_1682142677_bIHYG(x):
    with open('/dev/null', 'r'):
        PyCall_1682142677_JZrNJ(x)
