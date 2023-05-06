from calendar import *
import calendar
import argparse

def demoFunc(arg1,arg2,arg3,arg4):
    try:
        obj = calendar.TextCalendar()
        ret = obj.formatmonth(arg1,arg2,arg3,arg4)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
        pass

theyear=" 1106749140;00000000000000000000000000000000000000000000000000000000000000002"
themonth=11
w=11
l=8100000000
demoFunc(theyear,themonth,w,l)
