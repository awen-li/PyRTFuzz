from fuzzwrap import PyDecode 
from imaplib import *
import imaplib
import calendar
import getopt
import getpass
import re
import time
from io import DEFAULT_BUFFER_SIZE

API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        date_time = PyDecode(API_TYPE_LIST, arg)
        ret = imaplib.Time2Internaldate(date_time)
    except (AssertionError, AttributeError, IMAP4.error, ImportError, LookupError, OSError, TypeError, ValueError, calendar.IllegalMonthError, calendar.IllegalWeekdayError, getopt.GetoptError, getopt.error, getpass.GetPassWarning) as e:
        pass

def RunFuzzer(x):
    demoFunc(x)
