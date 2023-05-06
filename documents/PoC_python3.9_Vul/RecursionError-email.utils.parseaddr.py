from email.utils import *
import email
import email.utils
import re

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            ret = email.utils.parseaddr(arg)
        except (AttributeError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError):
            pass

with open("email.utils.parseaddr-arg.txt","r") as f:
    addr = f.readline()
    dc = demoCls()
    dc.demoFunc(addr)
