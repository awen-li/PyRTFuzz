
from pyclbr import *
import pyclbr
import io
import tokenize
from token import DEDENT
from token import NAME
from token import OP


def demoFunc(module):
    try:
        ret = pyclbr.readmodule_ex(module)
    except (AssertionError, AttributeError, ImportError, LookupError, OSError, StopIteration, TypeError, ValueError, tokenize.StopTokenizing, tokenize.TokenError) as e:
        pass

with open ("pyclbr.readmodule_ex-module", "r") as F:
    module = F.read ()
            
demoFunc(module)
