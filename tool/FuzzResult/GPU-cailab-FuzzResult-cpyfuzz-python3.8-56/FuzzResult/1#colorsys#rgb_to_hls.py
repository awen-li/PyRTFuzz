from fuzzwrap import PyDecode 
from colorsys import *
import colorsys

API_TYPE_LIST = ['float', 'float', 'float']

def demoFunc(arg):
    try:
        (r, g, b) = PyDecode(API_TYPE_LIST, arg)
        colorsys.rgb_to_hls(r, g, b)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681352789_SeXnO(x)

def PyCall_1681352789_SeXnO(x):
    demoFunc(x)
