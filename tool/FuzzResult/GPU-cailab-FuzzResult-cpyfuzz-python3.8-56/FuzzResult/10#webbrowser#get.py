from fuzzwrap import PyDecode 
from webbrowser import *
import webbrowser
import copy
import getopt
import shutil
import subprocess
import threading

API_TYPE_LIST = ['str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            using = PyDecode(API_TYPE_LIST, arg)
            ret = webbrowser.get(using)
        except (AssertionError, AttributeError, FileNotFoundError, KeyError, LookupError, NotADirectoryError, NotImplementedError, OSError, PermissionError, TypeError, ValueError, copy.Error, getopt.GetoptError, getopt.error, shutil.Error, shutil.ExecError, shutil.ReadError, shutil.RegistryError, shutil.SameFileError, shutil.SpecialFileError, subprocess.TimeoutExpired, threading.BrokenBarrierError, webbrowser.Error) as e:
            pass

def RunFuzzer(x):
    if True:
        W_U1 = 0
        while (W_U1 in range(0, 1)):
            W_U1 += 1
            PyCall_1682201552_vRlsB(x)

def PyCall_1682201552_vRlsB(x):
    W_d1 = 0
    while (W_d1 in range(0, 1)):
        W_d1 += 1
        W_C1 = 0
        while (W_C1 in range(0, 1)):
            W_C1 += 1
            if True:
                with open('/dev/null', 'r'):
                    W_S1 = 0
                    while (W_S1 in range(0, 1)):
                        W_S1 += 1
                        W_J1 = 0
                        while (W_J1 in range(0, 1)):
                            W_J1 += 1
                            dc = demoCls()
                            dc.demoFunc(x)
