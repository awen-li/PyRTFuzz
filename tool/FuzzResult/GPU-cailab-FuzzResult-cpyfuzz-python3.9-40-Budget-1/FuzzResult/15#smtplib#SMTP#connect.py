from fuzzwrap import PyDecode 
from smtplib import *
import smtplib
import copy
import io
import re

CLS_TYPE_LIST = ['NoneType', 'NoneType', 'NoneType', 'NoneType', 'NoneType']
API_TYPE_LIST = ['str', 'int', 'NoneType']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = smtplib.SMTP()
            (host, port, source_address) = PyDecode(API_TYPE_LIST, arg)
            obj.connect(host, port, source_address)
            PyPrint(obj)
            repr(obj)
        except (AssertionError, AttributeError, ImportError, LookupError, OSError, RuntimeError, TypeError, UnicodeEncodeError, ValueError, copy.Error, smtplib.SMTPAuthenticationError, smtplib.SMTPConnectError, smtplib.SMTPDataError, smtplib.SMTPException, smtplib.SMTPHeloError, smtplib.SMTPNotSupportedError, smtplib.SMTPRecipientsRefused, smtplib.SMTPResponseException, smtplib.SMTPSenderRefused, smtplib.SMTPServerDisconnected) as e:
            pass

def RunFuzzer(x):
    PyCall_1682082902_Jzskq(x)

def PyCall_1682082902_QWylV(x):
    with open('/dev/null', 'r'):
        if True:
            with open('/dev/null', 'r'):
                dc = demoCls()
                dc.demoFunc(x)

def PyCall_1682082902_uvlya(x):
    PyCall_1682082902_QWylV(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682082902_Jzskq(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                if True:
                    with open('/dev/null', 'r'):
                        PyCall_1682082902_uvlya(x)
