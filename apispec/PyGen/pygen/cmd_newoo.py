
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

    def op_functiondef (self, node):
        if node.name != self.criterion.Name:
            return node

        # translate api code into ast
        InitStmt = ast.parse(self.init)
        if self.HasArgs (InitStmt.body[0]):
            raise Exception("Warning: unsopport parameters in construction function!")
        CallStmt = ast.parse(self.api.Expr)

        # get the FP of current node
        if self.criterion.NodeVal == None or self.criterion.NodeVal.Attr != NodeVal.NodeAttr_FP:
            raise Exception("Unspected value type!")
        fp = self.criterion.NodeVal.Val
        DebugPrint (self.criterion.Name + " formal paras: " + str(fp))

        # first edit the ast
        if self.HasArgs (CallStmt.body[0]):
            # data flow into the parameter 1 by default
            CallStmt.body[0].value.args[0] = self.op_new_value (fp[0])

        # then update the graph
        self.pG.pg_call (CallStmt.body[0].value, self.criterion)

        # encode new body
        if self.IsBlankBody (node.body):
            node.body = InitStmt.body
        node.body += CallStmt.body

        node.body = self.op_try_wrapper (node.body, ['TypeError', 'NameError'])
        
        return node

    def GenApp (self):
        self.criterion = self.GetWrapF ()
        if self.criterion == None:
            DebugPrint ("[GenApp] get the insert point fail!...")
            return
        self.criterion.View()
        DebugPrint ("GenApp -> api: " + self.init + "  " + self.api.Expr)
        
        astApp = ast.parse(NewOO.OOTmpt)
        DebugPrint (astunparse.unparse(astApp))
        new = self.visit(astApp)
        DebugPrint (astunparse.unparse(new))
        self.pG.ShowPg ()

        