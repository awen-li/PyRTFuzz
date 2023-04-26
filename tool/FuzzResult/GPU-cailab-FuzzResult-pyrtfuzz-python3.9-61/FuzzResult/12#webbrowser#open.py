from fuzzwrap import PyDecode 
from webbrowser import *
import webbrowser
import copy
import getopt
import shutil
import subprocess
import threading

API_TYPE_LIST = ['None', 'None', 'None']

def demoFunc(arg):
    try:
        (url, new, autoraise) = PyDecode(API_TYPE_LIST, arg)
        ret = webbrowser.open(url, new, autoraise)
    except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotADirectoryError, NotImplementedError, OSError, PermissionError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        PyCall_1682440730_SzYIE(x)

def PyCall_1682440730_xMrfj(x):
    demoFunc(x)

def PyCall_1682440730_LupPn(x):
    for F_u1 in range(0, 1):
        W_S1 = 0
        while (W_S1 in range(0, 1)):
            W_S1 += 1
            with open('/dev/null', 'r'):
                W_c1 = 0
                while (W_c1 in range(0, 1)):
                    W_c1 += 1
                    W_f1 = 0
                    while (W_f1 in range(0, 1)):
                        W_f1 += 1
                        PyCall_1682440730_xMrfj(x)

def PyCall_1682440730_SzYIE(x):
    with open('/dev/null', 'r'):
        PyCall_1682440730_LupPn(x)
