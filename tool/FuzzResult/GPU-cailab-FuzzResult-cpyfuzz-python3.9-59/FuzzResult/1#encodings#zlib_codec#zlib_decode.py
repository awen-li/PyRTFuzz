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
    dc = demoCls()
    dc.demoFunc(x)
