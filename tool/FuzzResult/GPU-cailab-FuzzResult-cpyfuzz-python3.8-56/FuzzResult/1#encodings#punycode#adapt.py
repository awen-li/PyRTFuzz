from fuzzwrap import PyDecode 
from encodings.punycode import *
import encodings
import encodings.punycode

API_TYPE_LIST = ['int', 'bool', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (delta, first, numchars) = PyDecode(API_TYPE_LIST, arg)
            ret = encodings.punycode.adapt(delta, first, numchars)
        except (AssertionError, AttributeError, IndexError, LookupError, OSError, TypeError, UnicodeError, ValueError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
