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
API_TYPE_LIST = ['Request', 'HTTPResponse']

def demoFunc(arg):
    try:
        obj = urllib.request.HTTPErrorProcessor()
        (request, response) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.http_response(request, response)
        repr(obj)
        PyPrint(obj)
    except (AssertionError, AttributeError, ContentTooShortError, HTTPError, ImportError, KeyError, KeyboardInterrupt, LookupError, OSError, TypeError, URLError, ValueError, ftplib.Error, ftplib.error_perm, ftplib.error_proto, ftplib.error_reply, ftplib.error_temp, getpass.GetPassWarning, http.client.BadStatusLine, http.client.CannotSendHeader, http.client.CannotSendRequest, http.client.HTTPException, http.client.ImproperConnectionState, http.client.IncompleteRead, http.client.InvalidURL, http.client.LineTooLong, http.client.NotConnected, http.client.RemoteDisconnected, http.client.ResponseNotReady, http.client.UnimplementedFileMode, http.client.UnknownProtocol, http.client.UnknownTransferEncoding, socket.gaierror) as e:
        pass

def RunFuzzer(x):
    PyCall_1682236732_Xllhr(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682236732_tSvBC(x):
    if True:
        demoFunc(x)

def PyCall_1682236732_GihRx(x):
    with open('/dev/null', 'r'):
        PyCall_1682236732_tSvBC(x)

def PyCall_1682236732_jjDzG(x):
    PyCall_1682236732_GihRx(x)

def PyCall_1682236732_Xllhr(x):
    with open('/dev/null', 'r'):
        PyCall_1682236732_jjDzG(x)
