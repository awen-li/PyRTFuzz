from fuzzwrap import PyDecode 
from ast import *
import ast

API_TYPE_LIST = ['Constant']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            node_or_string = PyDecode(API_TYPE_LIST, arg)
            ret = ast.literal_eval(node_or_string)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681347997_iAuGG(x)

def PyCall_1681347997_iAuGG(x):
    dc = demoCls()
    dc.demoFunc(x)
