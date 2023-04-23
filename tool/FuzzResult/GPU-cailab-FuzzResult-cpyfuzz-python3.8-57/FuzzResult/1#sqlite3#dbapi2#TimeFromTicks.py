from fuzzwrap import PyDecode 
from sqlite3.dbapi2 import *
import sqlite3
import sqlite3.dbapi2

API_TYPE_LIST = ['int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            ticks = PyDecode(API_TYPE_LIST, arg)
            ret = sqlite3.dbapi2.TimeFromTicks(ticks)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
