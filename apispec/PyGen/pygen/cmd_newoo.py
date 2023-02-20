
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

    def demoFunc(self, arg):
        pass

def RunFuzzer (x):
    dc = demoCls ()
    dc.demoFunc (x)
"""
    def __init__(self):
        super(NewOO, self).__init__(NewOO.OOTmpt)
        self.init = None
        self.api  = None
        self.excepts = None
        self.criterion = None

    def SetUp (self, init, api, excepts, cls=None):
        self.cls  = cls
        self.init = init
        self.api  = api
        self.excepts = excepts
        
    def GenApp (self):
        self.criterion = self.GetWrapF ()
        if self.criterion == None:
            DebugPrint ("[GenApp] get the insert point fail!...")
            return
        self.criterion.View()
        DebugPrint ("GenApp -> api: " + str(self.init) + "  " + self.api.Expr)
        
        astApp = ast.parse(NewOO.OOTmpt)
        new = self.visit(astApp)

        # add api type list
        if self.api != None:
            new = self.op_type_list (new, self.api.Expr, self.init)
 
        DebugPrint (astunparse.unparse(new))
        self.pG.ShowPg ()
        return astunparse.unparse(new)

        