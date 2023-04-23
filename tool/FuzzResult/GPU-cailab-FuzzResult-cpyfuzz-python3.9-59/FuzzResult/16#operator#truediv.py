from fuzzwrap import PyDecode 
from operator import *
import operator

API_TYPE_LIST = ['int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (a, b) = PyDecode(API_TYPE_LIST, arg)
            ret = operator.truediv(a, b)
        except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681878498_gHocE(x)

def PyCall_1681878498_gHocE(x):
    for F_g1 in range(0, 1):
        with open('/dev/null', 'r'):
            if True:
                for F_u1 in range(0, 1):
                    with open('/dev/null', 'r'):
                        with open('/dev/null', 'r'):
                            for F_M1 in range(0, 1):
                                dc = demoCls()
                                dc.demoFunc(x)
