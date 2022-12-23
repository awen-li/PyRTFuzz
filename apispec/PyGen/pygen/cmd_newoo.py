
# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

class NewOO(AstOp):
    OOTmpt = \
"""
class demoCls:
    def __init__(self):
        pass

    def demoFunc1(self, arg1):
        pass

def RunFuzzer (x):
    dc = demoCls ()
    dc.demoFunc1 (x)
"""
    def __init__(self, init, api, excepts):
        super(NewOO, self).__init__(NewOO.OOTmpt)
        self.init = init
        self.api  = api
        self.excepts = excepts
        self.criterion = None

    def GenApp (self):
        self.criterion = self.GetWrapF ()
        if self.criterion == None:
            DebugPrint ("[GenApp] get the insert point fail!...")
            return
        self.criterion.View()
        DebugPrint ("GenApp -> api: " + self.init + "  " + self.api.Expr)
        
        astApp = ast.parse(NewOO.OOTmpt)
        new = self.visit(astApp)
        DebugPrint (astunparse.unparse(new))
        self.pG.ShowPg ()

        