from fuzzwrap import PyDecode 
from email.quoprimime import *
import email
import email.quoprimime
import re

API_TYPE_LIST = ['int']

def demoFunc(arg):
    try:
        octet = PyDecode(API_TYPE_LIST, arg)
        ret = email.quoprimime.body_check(octet)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    if True:
        demoFunc(x)
