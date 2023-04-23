from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['BufferedWriter']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = aifc.Aifc_write(None)
            file = PyDecode(API_TYPE_LIST, arg)
            obj.initfp(file)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682197880_CfXoY(x)

def PyCall_1682197880_vbkuJ(x):
    W_w1 = 0
    while (W_w1 in range(0, 1)):
        W_w1 += 1
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682197880_tcmcJ(x):
    for F_F1 in range(0, 1):
        PyCall_1682197880_vbkuJ(x)

def PyCall_1682197880_CfXoY(x):
    for F_K1 in range(0, 1):
        PyCall_1682197880_tcmcJ(x)
