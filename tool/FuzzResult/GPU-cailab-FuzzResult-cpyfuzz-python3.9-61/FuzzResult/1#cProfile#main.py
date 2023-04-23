from fuzzwrap import PyDecode 
from cProfile import *
import cProfile

API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            ret = cProfile.main()
        except (AssertionError, AttributeError, BrokenPipeError, KeyError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)
