
from string import *
import string
import re

def demoFunc(arg1,arg2):
    try:
        obj = string.Formatter()
        ret = obj.format_field(arg1, arg2)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

value = ")D"
format_spec = "9933333333"
demoFunc(value,format_spec)
