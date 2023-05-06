from distutils.fancy_getopt import *
import distutils
import distutils.fancy_getopt
import getopt
import re


class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg1,arg2):
        try:
            ret = distutils.fancy_getopt.wrap_text(arg1,arg2)
        except (AssertionError, AttributeError, DistutilsGetoptError, LookupError, OSError, RuntimeError, TypeError, ValueError, getopt.GetoptError, getopt.error) as e:
            pass


text = "CwW4#BWO&H1A191$4&۪%mn"
width = 0
dc = demoCls()
dc.demoFunc(text, width)
