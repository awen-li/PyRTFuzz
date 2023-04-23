from fuzzwrap import PyDecode 
from encodings.zlib_codec import *
import encodings
import encodings.zlib_codec
import zlib

API_TYPE_LIST = ['bytes', 'str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (input, errors) = PyDecode(API_TYPE_LIST, arg)
            encodings.zlib_codec.zlib_decode(input, errors)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    for F_A1 in range(0, 1):
        W_d1 = 0
        while (W_d1 in range(0, 1)):
            W_d1 += 1
            PyCall_1682263739_FHQUZ(x)

def PyCall_1682263739_vkcto(x):
    if True:
        if True:
            dc = demoCls()
            dc.demoFunc(x)

def PyCall_1682263739_FHQUZ(x):
    PyCall_1682263739_vkcto(x)
