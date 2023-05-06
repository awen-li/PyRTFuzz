
from codeop import *
import codeop

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, source, filename, symbol):
        try:
            ret = codeop.compile_command(source, filename, symbol)
        except (AssertionError, AttributeError, LookupError, OSError, SyntaxError, TypeError, ValueError) as e:
            pass

with open ("codeop.compile_command-source", "r") as F:
    source = F.read ()
with open ("codeop.compile_command-filename", "r") as F:
    filename = F.read ()
with open ("codeop.compile_command-symbol", "r") as F:
    symbol = F.read ()
    
dc = demoCls()
dc.demoFunc(source, filename, symbol)
