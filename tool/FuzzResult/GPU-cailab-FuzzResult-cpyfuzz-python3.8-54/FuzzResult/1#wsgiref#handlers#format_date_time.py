from fuzzwrap import PyDecode 
from wsgiref.handlers import *
import wsgiref
import time
import wsgiref.handlers

API_TYPE_LIST = ['float']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            timestamp = PyDecode(API_TYPE_LIST, arg)
            ret = wsgiref.handlers.format_date_time(timestamp)
        except (AssertionError, AttributeError, BrokenPipeError, ConnectionAbortedError, ConnectionResetError, LookupError, NotImplementedError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681352770_Amgwj(x)

def PyCall_1681352770_Amgwj(x):
    dc = demoCls()
    dc.demoFunc(x)
