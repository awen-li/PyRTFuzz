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
        except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotImplementedError, OSError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
            pass

def RunFuzzer(x):
    W_O1 = 0
    while (W_O1 in range(0, 1)):
        W_O1 += 1
        with open('/dev/null', 'r'):
            PyCall_1682245324_DWajA(x)

def PyCall_1682245324_qtAiH(x):
    dc = demoCls()
    dc.demoFunc(x)

def PyCall_1682245324_DWajA(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            PyCall_1682245324_qtAiH(x)
