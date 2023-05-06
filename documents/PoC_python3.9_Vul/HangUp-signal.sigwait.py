from fuzzwrap import PyDecode 
from signal import *
import signal

API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            ret = signal.sigwait(arg)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass


sigset =""
dc = demoCls()
dc.demoFunc(sigset)
