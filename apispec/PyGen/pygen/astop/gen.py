
import os
import astunparse
from .astop import *


pg_tempt_oo = \
"""
class demoCls:
    def __init__(self):
        pass

    def demoFunc0(self):
        pass

    def demoFunc1(self, PYF_ARG1):
        pass

def RunFuzzer (x):
    pass
"""

pg_tempt_pro = \
"""
def demoFunc0 ():
    pass

def demoFunc1 (PYF_ARG1):
    pass

def RunFuzzer (x):
    pass
"""

pg_for = \
"""
for PYF_I in range (0, PYF_E):
    pass
"""

#####################################################################################################
#####################################################################################################

class AppGen ():
    def __init__ (self):
        pass

    def Gen (self):
        Ast = ast.parse(pg_tempt_oo)
        print ("=============   original source   =============\r\n")

        ap = AstOp ()
        ap.visit (Ast)


