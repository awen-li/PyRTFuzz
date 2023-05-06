
from secrets import *
import secrets

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, nbytes):
        try:
            ret = secrets.token_hex(nbytes)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

dc = demoCls()
dc.demoFunc(2942742829)
