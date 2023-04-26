from fuzzwrap import PyDecode 
from webbrowser import *
import webbrowser
import copy
import getopt
import shutil
import subprocess
import threading

API_TYPE_LIST = ['None', 'None', 'None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (url, new, autoraise) = PyDecode(API_TYPE_LIST, arg)
            ret = webbrowser.open(url, new, autoraise)
        except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotADirectoryError, NotImplementedError, OSError, PermissionError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        if True:
            with open('/dev/null', 'r'):
                PyCall_1682316482_FlDTl(x)

def PyCall_1682316482_FlDTl(x):
    if True:
        with open('/dev/null', 'r'):
            with open('/dev/null', 'r'):
                if True:
                    with open('/dev/null', 'r'):
                        dc = demoCls()
                        dc.demoFunc(x)
