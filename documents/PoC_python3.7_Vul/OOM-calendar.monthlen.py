
from calendar import *
import calendar
import argparse


def demoFunc(year):
    try:
        ret = calendar.monthlen(year, 2)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
        pass
          
demoFunc("%9922623132d")
