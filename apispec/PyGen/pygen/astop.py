
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

    def op_new_tuple (self, list):
        return Tuple(elts=list)

    def op_new_excep_handler (self, excepTuple):
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
        DebugPrint (ast.dump (node), end="\n\n")
        for st in node.body:
            self.visit (st)
        return node

    def op_classdef(self, node):
        DebugPrint (ast.dump (node), end="\n\n")
        for st in node.body:
            self.visit (st)
        return node

