from fuzzwrap import PyDecode 
from binhex import *
import binhex
import binascii
import io

API_TYPE_LIST = ['str', 'str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (inp, out) = PyDecode(API_TYPE_LIST, arg)
            binhex.binhex(inp, out)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, binascii.Incomplete, binhex.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1681877780_tXzgN(x)

def PyCall_1681877780_tXzgN(x):
    dc = demoCls()
    dc.demoFunc(x)
