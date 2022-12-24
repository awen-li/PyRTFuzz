
# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

class NewPO(AstOp):
    POTmpt = \
"""
def demoFunc1(arg1):
    pass

def RunFuzzer (x):
    demoFunc1 (x)
"""
    def __init__(self):
        super(NewPO, self).__init__(NewPO.POTmpt)
        self.init = None
        self.api  = None
        self.excepts = None
        self.criterion = None

    def SetUp (self, init, api, excepts):
        self.init = init
        self.api  = api
        self.excepts = excepts

    def GenApp (self):
        if self.api == None:
            return
        
        self.criterion = self.GetWrapF ()
        if self.criterion == None:
            DebugPrint ("[GenApp] get the insert point fail!...")
            return
        self.criterion.View()
        DebugPrint ("GenApp -> api: " + self.init + "  " + self.api.Expr)
        
        astApp = ast.parse(NewPO.POTmpt)
        new = self.visit(astApp)
        DebugPrint (astunparse.unparse(new))
        self.pG.ShowPg ()

        