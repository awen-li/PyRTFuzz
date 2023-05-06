from calendar import *
import calendar
import argparse


def demoFunc(arg1,arg2):
    try:
        obj = calendar.TextCalendar()
        ret = obj.formatweekday(arg1,arg2)
        repr(obj)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
        pass


day =  3
width = 3732907367362
demoFunc(day, width)
