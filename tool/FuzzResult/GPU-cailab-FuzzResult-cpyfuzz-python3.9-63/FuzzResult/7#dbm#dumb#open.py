from fuzzwrap import PyDecode 
from dbm.dumb import *
import dbm
import dbm.dumb
import io

API_TYPE_LIST = ['str', 'str', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (file, flag, mode) = PyDecode(API_TYPE_LIST, arg)
            ret = dbm.dumb.open(file, flag, mode)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                if True:
                    dc = demoCls()
                    dc.demoFunc(x)
