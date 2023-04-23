from fuzzwrap import PyDecode 
from smtpd import *
import smtpd
import asyncore
import getopt
import smtplib
from io import StringIO

API_TYPE_LIST = ['None', 'None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (code, msg) = PyDecode(API_TYPE_LIST, arg)
            smtpd.usage(code, msg)
        except (AssertionError, AttributeError, ImportError, KeyboardInterrupt, LookupError, NotImplementedError, OSError, PermissionError, TypeError, ValueError, asyncore.ExitNow, getopt.GetoptError, getopt.error, smtplib.SMTPAuthenticationError, smtplib.SMTPConnectError, smtplib.SMTPDataError, smtplib.SMTPException, smtplib.SMTPHeloError, smtplib.SMTPNotSupportedError, smtplib.SMTPRecipientsRefused, smtplib.SMTPResponseException, smtplib.SMTPSenderRefused, smtplib.SMTPServerDisconnected) as e:
            pass

def RunFuzzer(x):
    PyCall_1681352789_TseCY(x)

def PyCall_1681352789_TseCY(x):
    dc = demoCls()
    dc.demoFunc(x)
