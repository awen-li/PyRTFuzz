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
    PyCall_1681718317_zzohO(x)

def PyCall_1681718317_QLglk(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1681718317_zzohO(x):
    if True:
        with open('/dev/null', 'r'):
            PyCall_1681718317_QLglk(x)
