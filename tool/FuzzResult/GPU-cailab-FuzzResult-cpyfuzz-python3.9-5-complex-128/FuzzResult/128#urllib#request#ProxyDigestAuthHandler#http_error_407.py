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

def demoFunc(arg):
    try:
        obj = urllib.request.ProxyDigestAuthHandler()
        (req, fp, code, msg, headers) = PyDecode(API_TYPE_LIST, arg)
        ret = obj.http_error_407(req, fp, code, msg, headers)
        PyPrint(obj)
        repr(obj)
    except (AssertionError, AttributeError, ContentTooShortError, HTTPError, ImportError, KeyError, KeyboardInterrupt, LookupError, OSError, TypeError, URLError, ValueError, ftplib.Error, ftplib.error_perm, ftplib.error_proto, ftplib.error_reply, ftplib.error_temp, getpass.GetPassWarning, http.client.BadStatusLine, http.client.CannotSendHeader, http.client.CannotSendRequest, http.client.HTTPException, http.client.ImproperConnectionState, http.client.IncompleteRead, http.client.InvalidURL, http.client.LineTooLong, http.client.NotConnected, http.client.RemoteDisconnected, http.client.ResponseNotReady, http.client.UnimplementedFileMode, http.client.UnknownProtocol, http.client.UnknownTransferEncoding, socket.gaierror) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        for F_I1 in range(0, 1):
            W_f1 = 0
            while (W_f1 in range(0, 1)):
                W_f1 += 1
                for F_u1 in range(0, 1):
                    if True:
                        W_K1 = 0
                        while (W_K1 in range(0, 1)):
                            W_K1 += 1
                            with open('/dev/null', 'r'):
                                with open('/dev/null', 'r'):
                                    for F_Y1 in range(0, 1):
                                        W_H1 = 0
                                        while (W_H1 in range(0, 1)):
                                            W_H1 += 1
                                            for F_p1 in range(0, 1):
                                                PyCall_1682163018_nFCCH(x)

def PyPrint(obj):
    with open('/dev/null', 'w') as F:
        print(obj, file=F)

def PyCall_1682163014_GqTTq(x):
    if True:
        if True:
            demoFunc(x)

def PyCall_1682163014_ESneq(x):
    PyCall_1682163014_GqTTq(x)

def PyCall_1682163014_OwaJT(x):
    with open('/dev/null', 'r'):
        PyCall_1682163014_ESneq(x)

def PyCall_1682163014_KOasv(x):
    W_R1 = 0
    while (W_R1 in range(0, 1)):
        W_R1 += 1
        W_f1 = 0
        while (W_f1 in range(0, 1)):
            W_f1 += 1
            if True:
                W_U1 = 0
                while (W_U1 in range(0, 1)):
                    W_U1 += 1
                    W_p1 = 0
                    while (W_p1 in range(0, 1)):
                        W_p1 += 1
                        W_U1 = 0
                        while (W_U1 in range(0, 1)):
                            W_U1 += 1
                            PyCall_1682163014_OwaJT(x)

def PyCall_1682163014_HXNhO(x):
    PyCall_1682163014_KOasv(x)

def PyCall_1682163015_FZneH(x):
    W_Q1 = 0
    while (W_Q1 in range(0, 1)):
        W_Q1 += 1
        W_e1 = 0
        while (W_e1 in range(0, 1)):
            W_e1 += 1
            if True:
                W_W1 = 0
                while (W_W1 in range(0, 1)):
                    W_W1 += 1
                    PyCall_1682163014_HXNhO(x)

def PyCall_1682163015_RJrWX(x):
    W_k1 = 0
    while (W_k1 in range(0, 1)):
        W_k1 += 1
        for F_I1 in range(0, 1):
            for F_c1 in range(0, 1):
                with open('/dev/null', 'r'):
                    W_K1 = 0
                    while (W_K1 in range(0, 1)):
                        W_K1 += 1
                        with open('/dev/null', 'r'):
                            for F_f1 in range(0, 1):
                                with open('/dev/null', 'r'):
                                    W_I1 = 0
                                    while (W_I1 in range(0, 1)):
                                        W_I1 += 1
                                        W_X1 = 0
                                        while (W_X1 in range(0, 1)):
                                            W_X1 += 1
                                            W_V1 = 0
                                            while (W_V1 in range(0, 1)):
                                                W_V1 += 1
                                                with open('/dev/null', 'r'):
                                                    if True:
                                                        W_N1 = 0
                                                        while (W_N1 in range(0, 1)):
                                                            W_N1 += 1
                                                            if True:
                                                                if True:
                                                                    W_c1 = 0
                                                                    while (W_c1 in range(0, 1)):
                                                                        W_c1 += 1
                                                                        if True:
                                                                            for F_x1 in range(0, 1):
                                                                                for F_j1 in range(0, 1):
                                                                                    PyCall_1682163015_FZneH(x)

def PyCall_1682163015_uVBRP(x):
    with open('/dev/null', 'r'):
        PyCall_1682163015_RJrWX(x)

def PyCall_1682163016_xtrlG(x):
    for F_e1 in range(0, 1):
        PyCall_1682163015_uVBRP(x)

def PyCall_1682163016_etFNu(x):
    W_x1 = 0
    while (W_x1 in range(0, 1)):
        W_x1 += 1
        W_q1 = 0
        while (W_q1 in range(0, 1)):
            W_q1 += 1
            with open('/dev/null', 'r'):
                for F_w1 in range(0, 1):
                    if True:
                        W_E1 = 0
                        while (W_E1 in range(0, 1)):
                            W_E1 += 1
                            if True:
                                with open('/dev/null', 'r'):
                                    if True:
                                        if True:
                                            PyCall_1682163016_xtrlG(x)

def PyCall_1682163016_iSNZC(x):
    PyCall_1682163016_etFNu(x)

def PyCall_1682163017_orNMG(x):
    if True:
        for F_D1 in range(0, 1):
            W_W1 = 0
            while (W_W1 in range(0, 1)):
                W_W1 += 1
                with open('/dev/null', 'r'):
                    for F_X1 in range(0, 1):
                        with open('/dev/null', 'r'):
                            for F_d1 in range(0, 1):
                                W_h1 = 0
                                while (W_h1 in range(0, 1)):
                                    W_h1 += 1
                                    PyCall_1682163016_iSNZC(x)

def PyCall_1682163017_gmnLQ(x):
    W_X1 = 0
    while (W_X1 in range(0, 1)):
        W_X1 += 1
        W_y1 = 0
        while (W_y1 in range(0, 1)):
            W_y1 += 1
            W_b1 = 0
            while (W_b1 in range(0, 1)):
                W_b1 += 1
                if True:
                    if True:
                        with open('/dev/null', 'r'):
                            PyCall_1682163017_orNMG(x)

def PyCall_1682163018_nFCCH(x):
    for F_O1 in range(0, 1):
        for F_m1 in range(0, 1):
            W_t1 = 0
            while (W_t1 in range(0, 1)):
                W_t1 += 1
                PyCall_1682163017_gmnLQ(x)
