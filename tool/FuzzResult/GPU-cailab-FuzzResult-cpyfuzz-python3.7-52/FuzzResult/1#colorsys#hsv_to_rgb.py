from fuzzwrap import PyDecode 
from colorsys import *
import colorsys

API_TYPE_LIST = ['float', 'float', 'float']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (h, s, v) = PyDecode(API_TYPE_LIST, arg)
            colorsys.hsv_to_rgb(h, s, v)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681356754_pUsrP(x)

def PyCall_1681356754_pUsrP(x):
    dc = demoCls()
    dc.demoFunc(x)
