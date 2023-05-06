 
from calendar import *
import calendar
import argparse

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            ret = calendar.isleap(arg)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, calendar.IllegalMonthError, calendar.IllegalWeekdayError) as e:
            pass

year = b'%4444444444F'
dc = demoCls()
dc.demoFunc(year)
