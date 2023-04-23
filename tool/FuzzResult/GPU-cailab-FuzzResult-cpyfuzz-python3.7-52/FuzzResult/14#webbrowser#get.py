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
    except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotImplementedError, OSError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
        pass

def RunFuzzer(x):
    with open('/dev/null', 'r'):
        with open('/dev/null', 'r'):
            W_l1 = 0
            while (W_l1 in range(0, 1)):
                W_l1 += 1
                if True:
                    with open('/dev/null', 'r'):
                        for F_Q1 in range(0, 1):
                            with open('/dev/null', 'r'):
                                with open('/dev/null', 'r'):
                                    W_Z1 = 0
                                    while (W_Z1 in range(0, 1)):
                                        W_Z1 += 1
                                        PyCall_1682128409_BRsCV(x)

def PyCall_1682128409_xSBAb(x):
    demoFunc(x)

def PyCall_1682128409_BRsCV(x):
    PyCall_1682128409_xSBAb(x)
