from fuzzwrap import PyDecode 
from string import *
import string
import re

CLS_TYPE_LIST = []
API_TYPE_LIST = ['str', 'str']

def demoFunc(arg1,arg2):
    try:
        obj = string.Formatter()
        ret = obj.format_field(arg1, arg2)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

value = ")D"
format_spec = "33333333333333"
demoFunc(value,format_spec)
