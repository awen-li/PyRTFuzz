from fuzzwrap import PyDecode 
from colorsys import *
import colorsys

API_TYPE_LIST = ['float', 'float', 'float']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (r, g, b) = PyDecode(API_TYPE_LIST, arg)
            colorsys.rgb_to_hsv(r, g, b)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    W_C1 = 0
    while (W_C1 in range(0, 1)):
        W_C1 += 1
        if True:
            if True:
                if True:
                    dc = demoCls()
                    dc.demoFunc(x)
