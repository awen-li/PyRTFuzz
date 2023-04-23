from fuzzwrap import PyDecode 
from webbrowser import *
import webbrowser
import copy
import getopt
import shutil
import subprocess
import threading

CLS_TYPE_LIST = ['NoneType']
API_TYPE_LIST = ['None']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            obj = webbrowser.BaseBrowser()
            url = PyDecode(API_TYPE_LIST, arg)
            ret = obj.open_new_tab(url)
            repr(obj)
        except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotImplementedError, OSError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
            pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682256462_SydDJ(x)

def PyCall_1682256462_SydDJ(x):
    dc = demoCls()
    dc.demoFunc(x)
