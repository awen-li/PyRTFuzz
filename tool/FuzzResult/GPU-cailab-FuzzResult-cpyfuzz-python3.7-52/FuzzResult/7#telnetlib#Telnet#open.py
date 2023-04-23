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
    PyCall_1681981342_BwxJj(x)

def PyCall_1681981342_dXxRj(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                dc = demoCls()
                dc.demoFunc(x)

def PyCall_1681981342_BwxJj(x):
    with open('/dev/null', 'r'):
        PyCall_1681981342_dXxRj(x)
