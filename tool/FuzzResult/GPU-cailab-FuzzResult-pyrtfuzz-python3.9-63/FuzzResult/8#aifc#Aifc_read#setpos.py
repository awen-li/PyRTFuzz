from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        obj = aifc.Aifc_read(None)
        pos = PyDecode(API_TYPE_LIST, arg)
        obj.setpos(pos)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    W_R1 = 0
    while (W_R1 in range(0, 1)):
        W_R1 += 1
        if True:
            with open('/dev/null', 'r'):
                W_j1 = 0
                while (W_j1 in range(0, 1)):
                    W_j1 += 1
                    W_Y1 = 0
                    while (W_Y1 in range(0, 1)):
                        W_Y1 += 1
                        with open('/dev/null', 'r'):
                            demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
