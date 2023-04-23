from fuzzwrap import PyDecode 
from xmlrpc.client import *
import xmlrpc
import gzip
import http.client
import xmlrpc.client
from io import BytesIO

CLS_TYPE_LIST = ['NoneType', 'NoneType']
API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = xmlrpc.client.Unmarshaller()
            data = PyDecode(API_TYPE_LIST, arg)
            obj.end_dateTime(data)
            repr(obj)
        except (AssertionError, AttributeError, Exception, ImportError, KeyError, LookupError, NotImplementedError, OSError, OverflowError, TypeError, ValueError, gzip.BadGzipFile, http.client.BadStatusLine, http.client.CannotSendHeader, http.client.CannotSendRequest, http.client.HTTPException, http.client.ImproperConnectionState, http.client.IncompleteRead, http.client.InvalidURL, http.client.LineTooLong, http.client.NotConnected, http.client.RemoteDisconnected, http.client.ResponseNotReady, http.client.UnimplementedFileMode, http.client.UnknownProtocol, http.client.UnknownTransferEncoding, xmlrpc.client.Error, xmlrpc.client.Fault, xmlrpc.client.ProtocolError, xmlrpc.client.ResponseError) as e:
            pass

def RunFuzzer(x):
    dc = demoCls()
    dc.demoFunc(x)
