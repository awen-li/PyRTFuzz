from fuzzwrap import PyDecode 
from telnetlib import *
import telnetlib
import re
from time import monotonic

CLS_TYPE_LIST = ['NoneType', 'NoneType', 'NoneType']
API_TYPE_LIST = ['None', 'None']

def demoFunc(arg):
    try:
        obj = telnetlib.Telnet()
        (list, timeout) = PyDecode(API_TYPE_LIST, arg)
        obj.expect(list, timeout)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
