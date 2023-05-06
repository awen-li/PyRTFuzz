from pydoc import *
import pydoc
import getopt
import io
import re
import threading
import tokenize
import webbrowser


class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg1,arg2,arg3,arg4):
        try:
            ret = pydoc.render_doc(arg1,arg2,arg3,arg4)
        except (AssertionError, AttributeError, EOFError, Exception, ImportError, KeyError, KeyboardInterrupt, LookupError, OSError, SyntaxError, TypeError, ValueError, getopt.GetoptError, pydoc.ErrorDuringImport, threading.BrokenBarrierError, tokenize.StopTokenizing, tokenize.TokenError, webbrowser.Error) as e:
            pass

thing= type("")
title= "fm#SFl2i@)4M333333Eb140%3333333333333handle_bus3333333333333333333%&$hbool"
forceload= "fm#SFl6yz*C)4_frequency_threshold'"
renderer= b'!@#$%^&*9523'
dc = demoCls()
dc.demoFunc(thing, title, forceload, renderer)
