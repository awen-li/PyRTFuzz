from fuzzwrap import PyDecode 
from socket import *
import socket
import io

API_TYPE_LIST = ['int', 'AddressFamily', 'SocketKind', 'int']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (fd, family, type, proto) = PyDecode(API_TYPE_LIST, arg)
            ret = socket.fromfd(fd, family, type, proto)
        except (AssertionError, AttributeError, BlockingIOError, ImportError, InterruptedError, LookupError, NameError, OSError, TypeError, ValueError) as e:
            pass

def RunFuzzer(x):
    if True:
        dc = demoCls()
        dc.demoFunc(x)
