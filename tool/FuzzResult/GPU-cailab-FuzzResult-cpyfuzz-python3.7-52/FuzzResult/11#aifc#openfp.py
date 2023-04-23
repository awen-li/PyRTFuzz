from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

API_TYPE_LIST = ['str', 'str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (f, mode) = PyDecode(API_TYPE_LIST, arg)
            ret = aifc.openfp(f, mode)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                with open('/dev/null', 'r'):
                    if True:
                        PyCall_1682237723_kXoTG(x)

def PyCall_1682237723_kXoTG(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                dc = demoCls()
                dc.demoFunc(x)
