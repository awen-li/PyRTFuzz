from fuzzwrap import PyDecode 
from calendar import *
import calendar
import argparse

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = calendar.Calendar()
            (year, width) = PyDecode(API_TYPE_LIST, arg)
            ret = obj.yeardatescalendar(year, width)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)
