from fuzzwrap import PyDecode 
from nntplib import *
import nntplib
import argparse
import netrc
import re
from email.header import decode_header

API_TYPE_LIST = ['str']

def demoFunc(arg):
    try:
        header_str = PyDecode(API_TYPE_LIST, arg)
        ret = nntplib.decode_header(header_str)
    except (AssertionError, AttributeError, EOFError, ImportError, LookupError, OSError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError, netrc.NetrcParseError, nntplib.NNTPDataError, nntplib.NNTPError, nntplib.NNTPPermanentError, nntplib.NNTPProtocolError, nntplib.NNTPReplyError, nntplib.NNTPTemporaryError) as e:
        pass

def RunFuzzer(x):
    if True:
        demoFunc(x)
