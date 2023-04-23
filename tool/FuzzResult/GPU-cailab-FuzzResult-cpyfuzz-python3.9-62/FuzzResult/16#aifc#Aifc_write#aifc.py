from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

def demoFunc(arg):
    try:
        obj = aifc.Aifc_write(None)
        obj.aifc()
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    PyCall_1682263225_homNx(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682263225_FaNnF(x):
    if True:
        W_f1 = 0
        while (W_f1 in range(0, 1)):
            W_f1 += 1
            with open('/dev/null', 'r'):
                with open('/dev/null', 'r'):
                    demoFunc(x)

def PyCall_1682263225_homNx(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                for F_W1 in range(0, 1):
                    if True:
                        PyCall_1682263225_FaNnF(x)
