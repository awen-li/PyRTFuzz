from fuzzwrap import PyDecode 
from sqlite3.dbapi2 import *
import sqlite3
import sqlite3.dbapi2

API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        ticks = PyDecode(API_TYPE_LIST, arg)
        ret = sqlite3.dbapi2.TimeFromTicks(ticks)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    for F_s1 in range(0, 1):
        PyCall_1681718276_UtDHF(x)

def PyCall_1681718276_szRqq(x):
    demoFunc(x)

def PyCall_1681718276_UtDHF(x):
    PyCall_1681718276_szRqq(x)
