from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_write(None)
        ret = obj.getmarkers()
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        for F_H1 in range(0, 1):
            W_h1 = 0
            while (W_h1 in range(0, 1)):
                W_h1 += 1
                PyCall_1682151587_WsBuc(x)

def PyCall_1682151587_DGkVl(x):
    for F_O1 in range(0, 1):
        demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682151587_WsBuc(x):
    PyCall_1682151587_DGkVl(x)
