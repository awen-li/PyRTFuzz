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
    W_a1 = 0
    while (W_a1 in range(0, 1)):
        W_a1 += 1
        for F_N1 in range(0, 1):
            PyCall_1681877768_eHCzO(x)

def PyCall_1681877768_eHCzO(x):
    demoFunc(x)
