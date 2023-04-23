from fuzzwrap import PyDecode 
from signal import *
import signal

API_TYPE_LIST = ['Signals', 'Handlers']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (signalnum, handler) = PyDecode(API_TYPE_LIST, arg)
            ret = signal.signal(signalnum, handler)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
