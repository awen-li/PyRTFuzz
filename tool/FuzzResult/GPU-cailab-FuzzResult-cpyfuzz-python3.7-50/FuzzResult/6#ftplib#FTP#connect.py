from fuzzwrap import PyDecode 
from ftplib import *
import ftplib
import re

CLS_TYPE_LIST = ['NoneType', 'NoneType', 'NoneType', 'NoneType', 'NoneType', 'NoneType']
API_TYPE_LIST = ['str', 'int', 'int', 'tuple']

def demoFunc(arg):
    try:
        obj = ftplib.FTP()
        (host, port, timeout, source_address) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.connect(host, port, timeout, source_address)
        repr(obj)
    except (AssertionError, AttributeError, EOFError, ImportError, LookupError, OSError, TypeError, ValueError, ftplib.Error, ftplib.error_perm, ftplib.error_proto, ftplib.error_reply, ftplib.error_temp) as e:
        pass

def RunFuzzer(x):
    for F_G1 in range(0, 1):
        W_v1 = 0
        while (W_v1 in range(0, 1)):
            W_v1 += 1
            W_u1 = 0
            while (W_u1 in range(0, 1)):
                W_u1 += 1
                with open('/dev/null', 'r'):
                    with open('/dev/null', 'r'):
                        demoFunc(x)
