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
            ret = sqlite3.dbapi2.DateFromTicks(ticks)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    for F_L1 in range(0, 1):
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                with open('/dev/null', 'r'):
                    for F_d1 in range(0, 1):
                        dc = demoCls()
                        dc.demoFunc(x)
