from fuzzwrap import PyDecode 
from socket import *
import socket
import io
import os

API_TYPE_LIST = ['str', 'int', 'int', 'SocketKind', 'int', 'int']

def demoFunc(arg):
    try:
        (host, port, family, type, proto, flags) = PyDecode(API_TYPE_LIST, arg)
        ret = socket.getaddrinfo(host, port, family, type, proto, flags)
    except (AssertionError, AttributeError, BlockingIOError, ImportError, InterruptedError, LookupError, NameError, OSError, TypeError, ValueError) as e:
        pass

def RunFuzzer(x):
    if True:
        demoFunc(x)
