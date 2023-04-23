from fuzzwrap import PyDecode 
from smtplib import *
import smtplib
import copy
import io
import re

CLS_TYPE_LIST = ['NoneType', 'NoneType', 'NoneType', 'NoneType', 'NoneType']
API_TYPE_LIST = ['str', 'int', 'NoneType']

def demoFunc(arg):
    try:
        obj = smtplib.SMTP()
        (host, port, source_address) = PyDecode(API_TYPE_LIST, arg)
        obj.connect(host, port, source_address)
        PyPrint(obj)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, RuntimeError, TypeError, UnicodeEncodeError, ValueError, copy.Error, smtplib.SMTPAuthenticationError, smtplib.SMTPConnectError, smtplib.SMTPDataError, smtplib.SMTPException, smtplib.SMTPHeloError, smtplib.SMTPNotSupportedError, smtplib.SMTPRecipientsRefused, smtplib.SMTPResponseException, smtplib.SMTPSenderRefused, smtplib.SMTPServerDisconnected) as e:
        pass

def RunFuzzer(x):
    W_K1 = 0
    while (W_K1 in range(0, 1)):
        W_K1 += 1
        with open('/dev/null', 'r'):
            for F_s1 in range(0, 1):
                with open('/dev/null', 'r'):
                    PyCall_1682238952_GMNTr(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682238952_GMNTr(x):
    for F_f1 in range(0, 1):
        if True:
            demoFunc(x)
