from calendar import *
import calendar
import argparse

def demoFunc(day, width):
    try:
        obj = calendar.TextCalendar()
        ret = obj.formatweekday(day, width)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
            pass

demoFunc (2, 9729990411)