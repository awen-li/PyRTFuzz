from fuzzwrap import PyDecode 
from xmlrpc.client import *
import xmlrpc
import gzip
import http.client
import xmlrpc.client
from io import BytesIO

API_TYPE_LIST = ['str']

def demoFunc(arg):
    try:
        s = PyDecode(API_TYPE_LIST, arg)
        ret = xmlrpc.client.escape(s)
    except (AssertionError, AttributeError, Exception, ImportError, KeyError, LookupError, NotImplementedError, OSError, OverflowError, TypeError, ValueError, gzip.BadGzipFile, http.client.BadStatusLine, http.client.CannotSendHeader, http.client.CannotSendRequest, http.client.HTTPException, http.client.ImproperConnectionState, http.client.IncompleteRead, http.client.InvalidURL, http.client.LineTooLong, http.client.NotConnected, http.client.RemoteDisconnected, http.client.ResponseNotReady, http.client.UnimplementedFileMode, http.client.UnknownProtocol, http.client.UnknownTransferEncoding, xmlrpc.client.Error, xmlrpc.client.Fault, xmlrpc.client.ProtocolError, xmlrpc.client.ResponseError) as e:
        pass

def RunFuzzer(x):
    if True:
        demoFunc(x)
