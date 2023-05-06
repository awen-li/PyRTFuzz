
from operator import *
import operator

def demoFunc(a, b):
    try:
        ret = operator.mul(a, b)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

demoFunc(192278862193, "!@#$%^&*9523")
