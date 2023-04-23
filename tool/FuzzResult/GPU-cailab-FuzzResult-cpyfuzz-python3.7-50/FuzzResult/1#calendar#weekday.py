from fuzzwrap import PyDecode 
from calendar import *
import calendar
import argparse

API_TYPE_LIST = ['int', 'int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (year, month, day) = PyDecode(API_TYPE_LIST, arg)
            ret = calendar.weekday(year, month, day)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
            pass

def RunFuzzer(x):
    PyCall_1681356750_ymbHb(x)

def PyCall_1681356750_ymbHb(x):
    dc = demoCls()
    dc.demoFunc(x)
