from fuzzwrap import PyDecode 
from email.utils import *
import email
import email.utils
import re

API_TYPE_LIST = ['str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, addr):
        try:
            ret = email.utils.parseaddr(addr)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError) as e:
            pass

with open ("email.utils.parseaddr-addr", "r") as F:
    x = F.read ()
dc = demoCls()
dc.demoFunc(x)
