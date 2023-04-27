from fuzzwrap import PyDecode 
from pprint import *
import pprint
import re
from io import StringIO

API_TYPE_LIST = ['int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            object = PyDecode(API_TYPE_LIST, arg)
            ret = pprint.isrecursive(object)
            PyPrint(obj)
        except (AssertionError, AttributeError, LookupError, OSError, StopIteration, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681880483_EkqRo(x)

def PyCall_1681880483_EkqRo(x):
    for F_z1 in range(0, 1):
        if True:
            dc = demoCls()
            dc.demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
