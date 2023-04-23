from fuzzwrap import PyDecode 
from sqlite3.dbapi2 import *
import sqlite3
import sqlite3.dbapi2

API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        ticks = PyDecode(API_TYPE_LIST, arg)
        ret = sqlite3.dbapi2.DateFromTicks(ticks)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        if True:
            demoFunc(x)
