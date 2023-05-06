
from calendar import *
import calendar
import argparse

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, theyear, themonth, w, l):
        try:
            obj = calendar.TextCalendar()
            obj.prmonth(theyear, themonth, w, l)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
            pass

theyear = 12484967
themonth = 6
w = 1927245712484967
l = 613

dc = demoCls()
dc.demoFunc(theyear, themonth, w, l)
