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
            repr(obj)
        except (AssertionError, AttributeError, LookupError, OSError, StopIteration, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    if True:
        PyCall_1682223321_jJwBX(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682223321_gpMzt(x):
    for F_S1 in range(0, 1):
        with open('/dev/null', 'r'):
            if True:
                if True:
                    for F_r1 in range(0, 1):
                        if True:
                            with open('/dev/null', 'r'):
                                for F_d1 in range(0, 1):
                                    for F_U1 in range(0, 1):
                                        for F_Y1 in range(0, 1):
                                            dc = demoCls()
                                            dc.demoFunc(x)

def PyCall_1682223321_jJwBX(x):
    PyCall_1682223321_gpMzt(x)
