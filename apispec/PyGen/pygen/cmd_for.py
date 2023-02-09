
# _*_ coding:utf-8 _*_
import random
import string
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

class PyFor(AstOp):

    ForRange = random.randint (1, 10)

    ForVar = random.choice (string.ascii_letters)
    ForVar = ForVar + str (ForRange)
    
    ForTmpt = \
f"""
def demoFunc1(arg1):
    for {ForVar} in range (0, {ForRange}):
        pass

def RunFuzzer (x):
    demoFunc1 (x)
"""
    def __init__(self):
        self.init = None
        self.api  = None
        self.excepts   = None
        self.criterion = None
        self.PyCode    = None
    
    def SetExeCode (self, ExeCode):
        self.PyCode = ExeCode
        if self.PyCode == None:
            super(PyFor, self).__init__(PyFor.ForTmpt)
        else:
            super(PyFor, self).__init__(self.PyCode)
    
    def SetUp (self, init, api, excepts):
        if self.PyCode != None:
            return
        self.init = init
        self.api  = api
        self.excepts = excepts

    def op_insert_apiinvoke (self, node, InitStmt, CallStmt):
        pyFor = node.body[0]
        DebugPrint (ast.dump (pyFor))
        if not isinstance (pyFor, For):
            print (ast.dump (pyFor))
            raise Exception("Warning: must be For stmt!")

        if self.IsBlankBody (pyFor.body):
            pyFor.body = InitStmt.body
        else:
            pyFor.body += InitStmt.body
        pyFor.body += CallStmt.body
        return node

    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node

        Range  = random.randint (1, 10)
        ForVar = random.choice (string.ascii_letters) + str (Range)
        forAst = ast.parse (f'for {ForVar} in range (0, {Range}):\
        pass').body[0]

        forAst.body = node.body
        node.body = [forAst]
        return node
        
    def GenApp (self):
        
        if self.PyCode == None:
            self.criterion = self.GetWrapF ()
            if self.criterion == None:
                DebugPrint ("[GenApp] get the insert point fail!...")
                return
            
            self.criterion.View()
            DebugPrint ("GenApp -> api: " + str(self.init) + "  " + self.api.Expr)
            
            astApp = ast.parse(PyFor.ForTmpt)
            new = self.visit(astApp)
            
            DebugPrint (astunparse.unparse(new))
            self.pG.ShowPg ()
            return astunparse.unparse(new)
        else:
            # we need to wrap the input code
            self.criterion = self.GetMainNode ()
            self.criterion.View()

            astApp = ast.parse(self.PyCode)
            new = self.visit(astApp)

            DebugPrint (astunparse.unparse(new))
            return astunparse.unparse(new)
        
        

        