from fuzzwrap import PyDecode 
from urllib.request import *
import urllib
import ftplib
import getpass
import http.client
import io
import re
import socket
import time
import urllib.request
from urllib.error import ContentTooShortError
from urllib.error import HTTPError
from urllib.error import URLError

API_TYPE_LIST = ['str', 'bytes', 'object']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (url, data, timeout) = PyDecode(API_TYPE_LIST, arg)
            ret = urllib.request.urlopen(url, data, timeout)
        except (AssertionError, AttributeError, ContentTooShortError, HTTPError, ImportError, KeyError, KeyboardInterrupt, LookupError, OSError, TypeError, URLError, ValueError, ftplib.Error, ftplib.error_perm, ftplib.error_proto, ftplib.error_reply, ftplib.error_temp, getpass.GetPassWarning, http.client.BadStatusLine, http.client.CannotSendHeader, http.client.CannotSendRequest, http.client.HTTPException, http.client.ImproperConnectionState, http.client.IncompleteRead, http.client.InvalidURL, http.client.LineTooLong, http.client.NotConnected, http.client.RemoteDisconnected, http.client.ResponseNotReady, http.client.UnimplementedFileMode, http.client.UnknownProtocol, http.client.UnknownTransferEncoding, socket.gaierror) as e:
            pass

def RunFuzzer(x):
    PyCall_1681352781_dQMjU(x)

def PyCall_1681352781_dQMjU(x):
    dc = demoCls()
    dc.demoFunc(x)
