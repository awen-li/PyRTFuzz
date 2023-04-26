from fuzzwrap import PyDecode 
from mimetypes import *
import mimetypes
import getopt

API_TYPE_LIST = ['NoneType']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            files = PyDecode(API_TYPE_LIST, arg)
            mimetypes.init(files)
        except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError, getopt.GetoptError, getopt.error) as e:
            pass

def RunFuzzer(x):
    PyCall_1681347991_JgrIl(x)

def PyCall_1681347991_JgrIl(x):
    dc = demoCls()
    dc.demoFunc(x)
