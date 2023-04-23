from fuzzwrap import PyDecode 
from site import *
import site
import io

API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            ret = site.check_enableusersite()
        except (AssertionError, AttributeError, Exception, ImportError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        try:
            Recursive(x)
        except (RecursionError,) as e:
            pass

def PyCall_1681356108_tIOgH(x):
    dc = demoCls()
    dc.demoFunc(x)

def Recursive(x):
    PyCall_1681356108_tIOgH(x)
    Recursive(x)
