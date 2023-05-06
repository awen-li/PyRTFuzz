
from socket import *
import socket
import io

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, buffering):
        try:
            obj = socket.socket()
            ret = obj.makefile("", buffering)
        except (AssertionError, AttributeError, BlockingIOError, ImportError, InterruptedError, LookupError, NameError, OSError, TypeError, ValueError) as e:
            pass

dc = demoCls()
dc.demoFunc(20000000000)
