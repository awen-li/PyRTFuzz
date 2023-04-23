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
    if True:
        if True:
            with open('/dev/null', 'r'):
                if True:
                    for F_P1 in range(0, 1):
                        with open('/dev/null', 'r'):
                            W_i1 = 0
                            while (W_i1 in range(0, 1)):
                                W_i1 += 1
                                PyCall_1682129510_dttkT(x)

def PyCall_1682129510_dttkT(x):
    with open('/dev/null', 'r'):
        W_U1 = 0
        while (W_U1 in range(0, 1)):
            W_U1 += 1
            demoFunc(x)
