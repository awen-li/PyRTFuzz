from fuzzwrap import PyDecode 
from email.message import *
import email
import email.message
import uu
from email import charset
from email import errors
from email import utils
from io import BytesIO
from io import StringIO

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['str', 'str']

def demoFunc(arg):
    try:
        obj = email.message.Message()
        (payload, charset) = PyDecode(API_TYPE_LIST, arg)
        obj.set_payload(payload, charset)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, UnicodeEncodeError, UnicodeError, ValueError, errors.HeaderParseError, uu.Error) as e:
        pass

def RunFuzzer(x):
    PyCall_1681347975_lLabh(x)

def PyCall_1681347975_lLabh(x):
    demoFunc(x)
