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
    W_N1 = 0
    while (W_N1 in range(0, 1)):
        W_N1 += 1
        if True:
            W_T1 = 0
            while (W_T1 in range(0, 1)):
                W_T1 += 1
                PyCall_1681635901_UqWXa(x)

def PyCall_1681635901_UqWXa(x):
    with open('/dev/null', 'r'):
        if True:
            W_T1 = 0
            while (W_T1 in range(0, 1)):
                W_T1 += 1
                demoFunc(x)
