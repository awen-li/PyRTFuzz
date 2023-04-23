from fuzzwrap import PyDecode 
from webbrowser import *
import webbrowser
import copy
import getopt
import shutil
import subprocess
import threading

API_TYPE_LIST = ['str']

def demoFunc(arg):
    try:
        using = PyDecode(API_TYPE_LIST, arg)
        ret = webbrowser.get(using)
    except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotADirectoryError, NotImplementedError, OSError, PermissionError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
        pass

def RunFuzzer(x):
    W_L1 = 0
    while (W_L1 in range(0, 1)):
        W_L1 += 1
        for F_C1 in range(0, 1):
            with open('/dev/null', 'r'):
                if True:
                    PyCall_1682099767_wCTvH(x)

def PyCall_1682099767_qCrYS(x):
    demoFunc(x)

def PyCall_1682099767_wCTvH(x):
    PyCall_1682099767_qCrYS(x)
