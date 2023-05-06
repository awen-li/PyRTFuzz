
from calendar import *
import calendar
import argparse


def demoFunc(day, weekday, width):
    try:
        obj = calendar.TextCalendar()
        ret = obj.formatday(day, weekday, width)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
        pass


demoFunc(3455770, 3910450021, 398773910450021)
