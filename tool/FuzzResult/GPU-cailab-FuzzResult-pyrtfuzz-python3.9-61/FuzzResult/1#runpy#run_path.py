from fuzzwrap import PyDecode 
from runpy import *
import runpy
import io

API_TYPE_LIST = ['str', 'dict', 'str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (path_name, init_globals, run_name) = PyDecode(API_TYPE_LIST, arg)
            ret = runpy.run_path(path_name, init_globals, run_name)
        except (AssertionError, AttributeError, ImportError, KeyError, LookupError, OSError, RuntimeError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
