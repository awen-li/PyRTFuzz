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
        except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotImplementedError, OSError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682222177_ffVak(x)

def PyCall_1682222177_ffVak(x):
    if True:
        if True:
            dc = demoCls()
            dc.demoFunc(x)
