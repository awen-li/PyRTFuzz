from fuzzwrap import PyDecode 
from genericpath import *
import genericpath

API_TYPE_LIST = ['int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (fp1, fp2) = PyDecode(API_TYPE_LIST, arg)
            ret = genericpath.sameopenfile(fp1, fp2)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
