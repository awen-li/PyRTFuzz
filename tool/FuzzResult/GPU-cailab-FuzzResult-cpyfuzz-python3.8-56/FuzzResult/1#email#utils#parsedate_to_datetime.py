from fuzzwrap import PyDecode 
from email.utils import *
import email
import datetime
import email.utils
import re
import time
from email._parseaddr import parsedate

API_TYPE_LIST = ['str']

def demoFunc(arg):
    try:
        data = PyDecode(API_TYPE_LIST, arg)
        ret = email.utils.parsedate_to_datetime(data)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError) as e:
        pass

def RunFuzzer(x):
    PyCall_1681352777_fSxtZ(x)

def PyCall_1681352777_fSxtZ(x):
    demoFunc(x)
