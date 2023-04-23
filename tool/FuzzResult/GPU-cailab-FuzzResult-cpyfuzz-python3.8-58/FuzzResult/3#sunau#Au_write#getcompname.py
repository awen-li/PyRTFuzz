from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = []

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_write(None)
            ret = obj.getcompname()
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        with open('/dev/null', 'r'):
            dc = demoCls()
            dc.demoFunc(x)
