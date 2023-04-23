from fuzzwrap import PyDecode 
from sunau import *
import sunau

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = sunau.Au_read(None)
            id = PyDecode(API_TYPE_LIST, arg)
            obj.getmark(id)
            repr(obj)
        except (AssertionError, AttributeError, EOFError, LookupError, OSError, TypeError, ValueError, sunau.Error) as e:
            pass

def RunFuzzer(x):
    W_p1 = 0
    while (W_p1 in range(0, 1)):
        W_p1 += 1
        W_S1 = 0
        while (W_S1 in range(0, 1)):
            W_S1 += 1
            with open('/dev/null', 'r'):
                dc = demoCls()
                dc.demoFunc(x)
