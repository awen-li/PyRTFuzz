from fuzzwrap import PyDecode 
from cProfile import *
import cProfile

API_TYPE_LIST = []

def demoFunc(arg):
    try:
        ret = cProfile.main()
    except (AssertionError, AttributeError, BrokenPipeError, KeyError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681352787_pKNxz(x)

def PyCall_1681352787_pKNxz(x):
    demoFunc(x)
