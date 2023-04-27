from fuzzwrap import PyDecode 
from calendar import *
import calendar
import argparse

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['int', 'int']

def demoFunc(arg):
    try:
        obj = calendar.Calendar()
        (year, width) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.yeardatescalendar(year, width)
        PyPrint(obj)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)
