from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int', 'int', 'bytes']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = aifc.Aifc_write(None)
            (id, pos, name) = PyDecode(API_TYPE_LIST, arg)
            obj.setmark(id, pos, name)
            repr(obj)
            PyPrint(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682201309_FoLiM(x)

def PyCall_1682201309_ogSLC(x):
    W_E1 = 0
    while (W_E1 in range(0, 1)):
        W_E1 += 1
        with open('/dev/null', 'r'):
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682201309_vhOke(x):
    PyCall_1682201309_ogSLC(x)

def PyCall_1682201309_UGAPb(x):
    PyCall_1682201309_vhOke(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682201309_buaiP(x):
    PyCall_1682201309_UGAPb(x)

def PyCall_1682201309_FoLiM(x):
    if True:
        PyCall_1682201309_buaiP(x)
