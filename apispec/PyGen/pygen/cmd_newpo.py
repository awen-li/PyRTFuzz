
# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

class NewPO(AstOp):
    POTmpt = \
"""
def demoFunc(arg):
    pass

def RunFuzzer (x):
    demoFunc (x)
"""
    def __init__(self):
        super(NewPO, self).__init__(NewPO.POTmpt)
        self.init = None
        self.api  = None
        self.excepts = None
        self.criterion = None

    def SetUp (self, init, api, excepts, cls=None):
        self.init = init
        self.api  = api
        self.excepts = excepts

    def GenApp (self):
        if self.api == None:
            DebugPrint ("[GenApp] api is None...")
            return None
        
        self.criterion = self.GetWrapF ()
        if self.criterion == None:
            DebugPrint ("[GenApp] get the insert point fail!...")
            return None
        self.criterion.View()
        DebugPrint ("GenApp -> api: " + str(self.init) + "  " + self.api.Expr)
        
        astApp = ast.parse(NewPO.POTmpt)
        new = self.visit(astApp)

        # add api type list
        if self.api != None:
            new = self.op_type_list (new, self.api.Expr, self.init)
        
        DebugPrint (astunparse.unparse(new))
        self.pG.ShowPg ()
        return astunparse.unparse(new)

        