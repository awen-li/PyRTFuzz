from fuzzwrap import PyDecode 
from webbrowser import *
import webbrowser
import copy
import getopt
import shutil
import subprocess
import threading

API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            url = PyDecode(API_TYPE_LIST, arg)
            ret = webbrowser.open_new(url)
        except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotADirectoryError, NotImplementedError, OSError, PermissionError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
            pass

def RunFuzzer(x):
    PyCall_1682157178_nHXNA(x)

def PyCall_1682157177_wEAgI(x):
    with open('/dev/null', 'r'):
        dc = demoCls()
        dc.demoFunc(x)

def PyCall_1682157178_TdmDm(x):
    with open('/dev/null', 'r'):
        if True:
            if True:
                PyCall_1682157177_wEAgI(x)

def PyCall_1682157178_nHXNA(x):
    PyCall_1682157178_TdmDm(x)
