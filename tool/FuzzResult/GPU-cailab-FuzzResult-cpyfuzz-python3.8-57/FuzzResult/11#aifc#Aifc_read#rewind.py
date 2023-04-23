from fuzzwrap import PyDecode 
from aifc import *
import aifc
import struct

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = aifc.Aifc_read(None)
            obj.rewind()
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, aifc.Error, struct.error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            with open('/dev/null', 'r'):
                PyCall_1682221248_QHKyq(x)

def PyCall_1682221248_QHKyq(x):
    if True:
        if True:
            if True:
                if True:
                    if True:
                        dc = demoCls()
                        dc.demoFunc(x)
