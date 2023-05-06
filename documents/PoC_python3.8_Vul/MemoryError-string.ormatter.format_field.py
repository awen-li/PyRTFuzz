
from string import *
import string
import re


def demoFunc(value, format_spec):
    try:
        obj = string.Formatter()
        ret = obj.format_field(value, format_spec)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass
 
value = "m6k]"
format_spec = "223222222222220222"
demoFunc(value, format_spec)
