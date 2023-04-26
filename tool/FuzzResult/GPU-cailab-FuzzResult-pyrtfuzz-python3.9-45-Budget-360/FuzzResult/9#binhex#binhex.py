from fuzzwrap import PyDecode 
from binhex import *
import binhex
import binascii
import io

API_TYPE_LIST = ['str', 'str']

def demoFunc(arg):
    try:
        (inp, out) = PyDecode(API_TYPE_LIST, arg)
        binhex.binhex(inp, out)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, binascii.Incomplete, binhex.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            if True:
                if True:
                    with open('/dev/null', 'r'):
                        PyCall_1681688829_MCNPD(x)

def PyCall_1681688829_MCNPD(x):
    if True:
        demoFunc(x)
