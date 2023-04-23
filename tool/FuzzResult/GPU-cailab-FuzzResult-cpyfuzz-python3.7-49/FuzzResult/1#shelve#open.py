from fuzzwrap import PyDecode 
from shelve import *
import shelve
from io import BytesIO

API_TYPE_LIST = ['str', 'str', 'int', 'bool']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (filename, flag, protocol, writeback) = PyDecode(API_TYPE_LIST, arg)
            ret = shelve.open(filename, flag, protocol, writeback)
        except (AssertionError, AttributeError, KeyError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)
