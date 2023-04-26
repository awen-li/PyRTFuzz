from fuzzwrap import PyDecode 
from urllib.request import *
import urllib
import ftplib
import getpass
import http.client
import io
import re
import socket
import urllib.request
from urllib.error import ContentTooShortError
from urllib.error import HTTPError
from urllib.error import URLError

CLS_TYPE_LIST = []
API_TYPE_LIST = ['Request', 'HTTPResponse', 'int', 'str', 'HTTPMessage']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = urllib.request.HTTPRedirectHandler()
            (req, fp, code, msg, headers) = PyDecode(API_TYPE_LIST, arg)
            ret = obj.http_error_302(req, fp, code, msg, headers)
            repr(obj)
        except (AssertionError, AttributeError, ContentTooShortError, HTTPError, ImportError, KeyError, KeyboardInterrupt, LookupError, OSError, TypeError, URLError, ValueError, ftplib.Error, ftplib.error_perm, ftplib.error_proto, ftplib.error_reply, ftplib.error_temp, getpass.GetPassWarning, http.client.BadStatusLine, http.client.CannotSendHeader, http.client.CannotSendRequest, http.client.HTTPException, http.client.ImproperConnectionState, http.client.IncompleteRead, http.client.InvalidURL, http.client.LineTooLong, http.client.NotConnected, http.client.RemoteDisconnected, http.client.ResponseNotReady, http.client.UnimplementedFileMode, http.client.UnknownProtocol, http.client.UnknownTransferEncoding, socket.gaierror) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            if True:
                PyCall_1681879513_kvGxi(x)

def PyCall_1681879513_JGFsR(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyCall_1681879513_MBfkw(x):
    if True:
        PyCall_1681879513_JGFsR(x)

def PyCall_1681879513_qVgsv(x):
    PyCall_1681879513_MBfkw(x)

def PyCall_1681879513_ryGxQ(x):
    if True:
        PyCall_1681879513_qVgsv(x)

def PyCall_1681879513_savNX(x):
    if True:
        PyCall_1681879513_ryGxQ(x)

def PyCall_1681879513_kvGxi(x):
    PyCall_1681879513_savNX(x)
