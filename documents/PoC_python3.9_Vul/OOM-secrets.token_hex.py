from secrets import *
import secrets

def demoFunc(arg):
    try:
        ret = secrets.token_hex(arg)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass


nbytes = 5177984211
demoFunc(nbytes)
