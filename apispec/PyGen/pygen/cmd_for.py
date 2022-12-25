
# _*_ coding:utf-8 _*_
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

class PyFor(AstOp):
    ForTmpt = \
"""
def demoFunc1(arg1):
    for i in range (0, 3):
        pass

def RunFuzzer (x):
    demoFunc1 (x)
"""
    def __init__(self, pyCode=None):
        self.PyCode = pyCode
        if pyCode == None:
            super(PyFor, self).__init__(PyFor.ForTmpt)
        else:
            super(PyFor, self).__init__(pyCode)
        
        self.init = None
        self.api  = None
        self.excepts = None
        self.criterion = None

    def SetUp (self, init, api, excepts):
        if self.PyCode != None:
            return
        self.init = init
        self.api  = api
        self.excepts = excepts

    def op_insert_apiinvoke (self, node, InitStmt, CallStmt):
        pyFor = node.body[0]
        print (ast.dump (pyFor))
        if not isinstance (pyFor, For):
            print (ast.dump (pyFor))
            raise Exception("Warning: must be For stmt!")

        if self.IsBlankBody (pyFor.body):
            pyFor.body = InitStmt.body
        else:
            pyFor.body += InitStmt.body
        pyFor.body += CallStmt.body
        return node
        
    def GenApp (self):
        
        if self.PyCode == None:
            self.criterion = self.GetWrapF ()
            if self.criterion == None:
                DebugPrint ("[GenApp] get the insert point fail!...")
                return
            
            self.criterion.View()
            DebugPrint ("GenApp -> api: " + self.init + "  " + self.api.Expr)
            
            astApp = ast.parse(PyFor.ForTmpt)
            new = self.visit(astApp)
            DebugPrint (astunparse.unparse(new))
            self.pG.ShowPg ()
        else:
            # we need to wrap the input code
            pass
        
        

        