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
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    W_E1 = 0
    while (W_E1 in range(0, 1)):
        W_E1 += 1
        W_J1 = 0
        while (W_J1 in range(0, 1)):
            W_J1 += 1
            if True:
                with open('/dev/null', 'r'):
                    if True:
                        if True:
                            for F_s1 in range(0, 1):
                                with open('/dev/null', 'r'):
                                    for F_O1 in range(0, 1):
                                        with open('/dev/null', 'r'):
                                            for F_K1 in range(0, 1):
                                                for F_Q1 in range(0, 1):
                                                    PyCall_1682120176_JbyCx(x)

def PyCall_1682120176_JbyCx(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)
