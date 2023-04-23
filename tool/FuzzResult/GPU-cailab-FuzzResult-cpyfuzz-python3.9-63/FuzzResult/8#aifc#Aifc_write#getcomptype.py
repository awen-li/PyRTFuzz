from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_write(None)
        ret = obj.getcomptype()
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            W_w1 = 0
            while (W_w1 in range(0, 1)):
                W_w1 += 1
                with open('/dev/null', 'r'):
                    PyCall_1682227635_qagNO(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682227635_qagNO(x):
    if True:
        demoFunc(x)
