
from calendar import *
import calendar
import argparse


def demoFunc(year):
    try:
        ret = calendar.isleap(year)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
        pass

demoFunc("{$%413784138823handle_usr172")
