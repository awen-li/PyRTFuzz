
from operator import *
import operator


def demoFunc(a, b):
    try:
        ret = operator.lshift(a, b)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, TypeError, ValueError) as e:
        pass

demoFunc(150299, 65029993111)
