from fuzzwrap import PyDecode 
from tabnanny import *
import tabnanny
import getopt
import tokenize

API_TYPE_LIST = ['None']

def demoFunc(arg):
    try:
        file = PyDecode(API_TYPE_LIST, arg)
        tabnanny.check(file)
    except (AssertionError, AttributeError, IndentationError, LookupError, OSError, TypeError, ValueError, getopt.GetoptError, getopt.error, tabnanny.NannyNag, tokenize.StopTokenizing, tokenize.TokenError) as e:
        pass

def RunFuzzer(x):
    W_H1 = 0
    while (W_H1 in range(0, 1)):
        W_H1 += 1
        W_X1 = 0
        while (W_X1 in range(0, 1)):
            W_X1 += 1
            W_h1 = 0
            while (W_h1 in range(0, 1)):
                W_h1 += 1
                demoFunc(x)
