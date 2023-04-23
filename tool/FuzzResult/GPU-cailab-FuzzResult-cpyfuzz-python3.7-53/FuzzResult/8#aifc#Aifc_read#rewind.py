from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        obj.rewind()
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682147602_sivEv(x)

def PyCall_1682147602_OBwCm(x):
    demoFunc(x)

def PyCall_1682147602_KaIRB(x):
    PyCall_1682147602_OBwCm(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682147602_sivEv(x):
    if True:
        with open('/dev/null', 'r'):
            W_s1 = 0
            while (W_s1 in range(0, 1)):
                W_s1 += 1
                PyCall_1682147602_KaIRB(x)
