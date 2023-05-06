from pyclbr import *
import pyclbr
import io
import tokenize
from token import DEDENT
from token import NAME
from token import OP

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg1,arg2):
        try:
            ret = pyclbr.readmodule_ex(arg1,arg2)
        except (AttributeError, ImportError, ModuleNotFoundError, OSError, StopIteration, TypeError, ValueError, tokenize.StopTokenizing, tokenize.TokenError):
            pass


module = '.'* 100_100
path = None
dc = demoCls()
dc.demoFunc(module, path)
