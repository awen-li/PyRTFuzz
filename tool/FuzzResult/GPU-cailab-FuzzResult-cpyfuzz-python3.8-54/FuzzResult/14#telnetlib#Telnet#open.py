from fuzzwrap import PyDecode 
from telnetlib import *
import telnetlib
import re
from time import monotonic

CLS_TYPE_LIST = ['NoneType', 'NoneType', 'NoneType']
API_TYPE_LIST = ['str', 'int', 'object']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = telnetlib.Telnet()
            (host, port, timeout) = PyDecode(API_TYPE_LIST, arg)
            obj.open(host, port, timeout)
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    for F_B1 in range(0, 1):
        with open('/dev/null', 'r'):
            W_y1 = 0
            while (W_y1 in range(0, 1)):
                W_y1 += 1
                W_n1 = 0
                while (W_n1 in range(0, 1)):
                    W_n1 += 1
                    PyCall_1682251776_MGkoO(x)

def PyCall_1682251776_huMmq(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682251776_MGkoO(x):
    if True:
        for F_X1 in range(0, 1):
            if True:
                W_Q1 = 0
                while (W_Q1 in range(0, 1)):
                    W_Q1 += 1
                    PyCall_1682251776_huMmq(x)
