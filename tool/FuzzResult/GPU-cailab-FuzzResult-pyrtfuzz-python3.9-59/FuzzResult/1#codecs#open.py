from fuzzwrap import PyDecode 
from codecs import *
import codecs

API_TYPE_LIST = ['str', 'str', 'str', 'str', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (filename, mode, encoding, errors, buffering) = PyDecode(API_TYPE_LIST, arg)
            ret = codecs.open(filename, mode, encoding, errors, buffering)
        except (AssertionError, AttributeError, ImportError, LookupError, NotImplementedError, OSError, StopIteration, TypeError, UnicodeDecodeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681348009_ExuoO(x)

def PyCall_1681348009_ExuoO(x):
    dc = demoCls()
    dc.demoFunc(x)
