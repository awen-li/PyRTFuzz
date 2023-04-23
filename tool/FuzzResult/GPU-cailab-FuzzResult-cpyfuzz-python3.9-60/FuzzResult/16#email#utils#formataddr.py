from fuzzwrap import PyDecode 
from email.utils import *
import email
import email.utils
import re

API_TYPE_LIST = ['tuple', 'str']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (pair, charset) = PyDecode(API_TYPE_LIST, arg)
            ret = email.utils.formataddr(pair, charset)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, UnicodeEncodeError, ValueError) as e:
            pass

def RunFuzzer(x):
    W_t1 = 0
    while (W_t1 in range(0, 1)):
        W_t1 += 1
        W_O1 = 0
        while (W_O1 in range(0, 1)):
            W_O1 += 1
            W_h1 = 0
            while (W_h1 in range(0, 1)):
                W_h1 += 1
                if True:
                    W_i1 = 0
                    while (W_i1 in range(0, 1)):
                        W_i1 += 1
                        for F_n1 in range(0, 1):
                            with open('/dev/null', 'r'):
                                for F_b1 in range(0, 1):
                                    with open('/dev/null', 'r'):
                                        with open('/dev/null', 'r'):
                                            if True:
                                                for F_V1 in range(0, 1):
                                                    W_V1 = 0
                                                    while (W_V1 in range(0, 1)):
                                                        W_V1 += 1
                                                        W_X1 = 0
                                                        while (W_X1 in range(0, 1)):
                                                            W_X1 += 1
                                                            dc = demoCls()
                                                            dc.demoFunc(x)
