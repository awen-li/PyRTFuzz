from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = aifc.Aifc_write(None)
            id = PyDecode(API_TYPE_LIST, arg)
            ret = obj.getmark(id)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682151564_BToYF(x)

def PyCall_1682151564_iHgXI(x):
    with open('/dev/null', 'r'):
        if True:
            W_h1 = 0
            while (W_h1 in range(0, 1)):
                W_h1 += 1
                with open('/dev/null', 'r'):
                    dc = demoCls()
                    dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682151564_YHBoT(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            for F_W1 in range(0, 1):
                W_H1 = 0
                while (W_H1 in range(0, 1)):
                    W_H1 += 1
                    PyCall_1682151564_iHgXI(x)

def PyCall_1682151564_BToYF(x):
    PyCall_1682151564_YHBoT(x)
