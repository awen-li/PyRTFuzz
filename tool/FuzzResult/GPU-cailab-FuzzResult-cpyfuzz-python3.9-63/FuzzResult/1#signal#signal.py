from fuzzwrap import PyDecode 
from signal import *
import signal

API_TYPE_LIST = ['Signals', 'Handlers']

def demoFunc(arg):
    try:
        (signalnum, handler) = PyDecode(API_TYPE_LIST, arg)
        ret = signal.signal(signalnum, handler)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
