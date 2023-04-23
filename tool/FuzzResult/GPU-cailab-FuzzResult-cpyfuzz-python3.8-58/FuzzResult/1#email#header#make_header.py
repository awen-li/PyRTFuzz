from fuzzwrap import PyDecode 
from email.header import *
import email
import binascii
import email.header
import re
from email.errors import HeaderParseError
from email import charset

API_TYPE_LIST = ['list', 'NoneType', 'NoneType', 'str']

def demoFunc(arg):
    try:
        (decoded_seq, maxlinelen, header_name, continuation_ws) = PyDecode(API_TYPE_LIST, arg)
        ret = email.header.make_header(decoded_seq, maxlinelen, header_name, continuation_ws)
    except (AssertionError, AttributeError, HeaderParseError, IndexError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError, binascii.Error) as e:
        pass

def RunFuzzer(x):
    if True:
        demoFunc(x)
