from fuzzwrap import PyDecode 
from colorsys import *
import colorsys

API_TYPE_LIST = ['float', 'float', 'float']

def demoFunc(arg):
    try:
        (h, s, v) = PyDecode(API_TYPE_LIST, arg)
        colorsys.hsv_to_rgb(h, s, v)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
