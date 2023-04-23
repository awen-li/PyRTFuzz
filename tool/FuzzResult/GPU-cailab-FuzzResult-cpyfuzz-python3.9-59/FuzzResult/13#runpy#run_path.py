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
    if True:
        if True:
            with open('/dev/null', 'r'):
                with open('/dev/null', 'r'):
                    with open('/dev/null', 'r'):
                        with open('/dev/null', 'r'):
                            if True:
                                if True:
                                    PyCall_1681878840_WqzZl(x)

def PyCall_1681878840_WqzZl(x):
    dc = demoCls()
    dc.demoFunc(x)
