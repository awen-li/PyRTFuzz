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
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682207690_aaDHU(x)

def PyCall_1682207690_pwXCq(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682207690_aaDHU(x):
    for F_H1 in range(0, 1):
        for F_T1 in range(0, 1):
            if True:
                for F_i1 in range(0, 1):
                    if True:
                        with open('/dev/null', 'r'):
                            for F_t1 in range(0, 1):
                                PyCall_1682207690_pwXCq(x)
