
from email.utils import *
import email
import email.utils
import re


class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, fieldvalues):
        try:
            ret = email.utils.getaddresses(fieldvalues)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError) as e:
            pass

with open ("email.utils.getaddresses-fieldvalues", "r") as F:
    fieldvalues = F.read ()
                
dc = demoCls()
dc.demoFunc(fieldvalues)
