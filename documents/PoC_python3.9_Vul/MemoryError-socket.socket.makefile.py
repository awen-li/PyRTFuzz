from socket import *
import socket
import io


class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg1,arg2):
        try:
            obj = socket.socket()
            ret = obj.makefile(arg1, arg2)
            repr(obj)
        except (AssertionError, AttributeError, BlockingIOError, ImportError, InterruptedError, LookupError, NameError, OSError, TypeError, ValueError) as e:
            pass

mode = ""
buffering = 3000000000534020970
dc = demoCls()
dc.demoFunc(mode,buffering)
