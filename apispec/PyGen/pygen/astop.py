
# _*_ coding:utf-8 _*_
import ast
from ast import *
from .propgraph import *
from .debug import *

def GetWrapF (pgNode):
    DebugPrint ("GetWrapF -> [%d]%s - %d" %(pgNode.Id, pgNode.Name, pgNode.Type))
    # must be a STMT
    if pgNode.Type != PropGraph.NodeType_STMT:
        return None
    
    #check call STMT with inputs
    if pgNode.NodeVal == None:
        return None

    #check value type: must be AP
    if pgNode.NodeVal.Attr != NodeVal.NodeAttr_AP or len (pgNode.NodeVal.Val) == 0:
        return None

    #get the def of the callee
    for oe in pgNode.OutEdge:
        if oe.Type != PropGraph.EdgeType_CALL:
            continue
        defNode = oe.DstNd
        return defNode
    
    return None

class AstOp (NodeTransformer):
    def __init__(self, Tmpt):
        self.Tmpt   = Tmpt
        self.pG     = PropGraph ()
        self.RootPg = self.pG.Build (self.Tmpt)

    def GetWrapF (self):
        for root in self.RootPg:
            if root.Type == PropGraph.NodeType_CLASS:
                # properity G entry
                continue
            return self.pG.VisitGp (GetWrapF, root, PropGraph.EdgeType_CFG)
        return None

    def IsBlankBody (self, body):
        if len (body) == 0:
            return True

        if len (body) == 1 and isinstance(body[0], Pass):
            return True

        return False


    def HasArgs (self, stmt):
        call = None
        if isinstance (stmt, Assign):
            call = stmt.value
        elif isinstance (stmt, Expr):
            call = stmt.value
        else:
            raise Exception("HasArgs -> Unsupport!!!")

        if len (call.args) == 0:
            return False
        else:
            return True
        
    def visit(self, node):
        if node is None:
            return

        method = 'op_' + node.__class__.__name__.lower()
        operator = getattr(self, method, self.generic_visit)        
        return operator(node)

    def op_new_value (self, name):
        return Name(id=name, ctx=Load())

    def op_new_try (self, stmts):
        return Try(body=stmts, handlers=[], orelse=[], finalbody=[])
        
    def op_new_tuple (self, list):
        return Tuple(elts=[self.op_new_value (i) for i in list])

    def op_new_excep_handler (self, excepList):
        excepTuple = self.op_new_tuple (excepList)
        return ExceptHandler(type=excepTuple)

    def op_value (self, node):
        return node
    
    def op_return(self, node):
        return node
    
    def op_assign(self, node):
        DebugPrint (ast.dump (node), end="\n\n")

        for tg in node.targets:
            self.visit (tg)
        
        return self.visit (node.value)

    def op_atrribute (self, node):
        return node

    def op_call(self, node):
        return node
    
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

        node.body = self.op_try_wrapper (node.body, self.excepts)
        
        return node

    def op_classdef(self, node):
        #DebugPrint (ast.dump (node), end="\n\n")
        for st in node.body:
            self.visit (st)
        return node


    def op_try_wrapper (self, targetBody, targetExceps):
        #body=[Try(body=[Pass()], 
        #      handlers=[ExceptHandler(type=Tuple(elts=[Name(id='NameError', ctx=Load()), Name(id='TypeError', ctx=Load())], ctx=Load()), name='error', body=[Pass()])]
        tryStmt = self.op_new_try(targetBody)
        handler = self.op_new_excep_handler(targetExceps)
        handler.body = [Pass()]
        tryStmt.handlers.append (handler)

        return [tryStmt]

