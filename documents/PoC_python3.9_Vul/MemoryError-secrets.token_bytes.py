from secrets import *
import secrets


class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            ret = secrets.token_bytes(arg)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass


nbytes = 555555555555555555
dc = demoCls()
dc.demoFunc(nbytes)
