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
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
        pass

def RunFuzzer(x):
    W_K1 = 0
    while (W_K1 in range(0, 1)):
        W_K1 += 1
        for F_q1 in range(0, 1):
            with open('/dev/null', 'r'):
                if True:
                    for F_K1 in range(0, 1):
                        for F_Y1 in range(0, 1):
                            for F_T1 in range(0, 1):
                                demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
