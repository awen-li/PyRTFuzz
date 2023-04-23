from fuzzwrap import PyDecode 
from bdb import *
import bdb

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None', 'None', 'None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = bdb.Bdb()
            (cmd, globals, locals) = PyDecode(API_TYPE_LIST, arg)
            obj.runctx(cmd, globals, locals)
        except (AssertionError, AttributeError, IndexError, LookupError, NotImplementedError, OSError, TypeError, ValueError, bdb.BdbQuit) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
