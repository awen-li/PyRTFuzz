
import ast
from ast import *
from .apptmpt import *

"""
Example:
class demoCls:
    def __init__(self):
        pass

    def demoFunc1(self, arg1):
        pass

def RunFuzzer (x):
    demoCls ().demoFunc1 (x)

-------------------------------------------------------------------
control flow graph:

               RunFuzzer (x)
                    |
          obj = demoCls.__init__()
                    |
             obj.demoFunc1 (x)

class graph:
                demoCls
                /     \
  __init__ (init)    demoFunc1 (x)
"""

class PgNode ():
    def __init__ (self, Id, Type):
        self.Id = Id
        self.InEdge = []
        self.OutEdge = []


class PgEdge ():
    def __init__ (self, Src, Dst):
        self.SrcNd = Src
        self.DstNd = Dst

        
class PropGraph (NodeVisitor):

    NodeId = 1
    
    def __init__ (self, MainFunc='RunFuzz'):
        self.MainFunc = MainFunc
        self.FuncList = {}
        self.Id2Node  = {}
        self.EdgeList = []

        self.CurClass = None

    def AddNode (self, Type):
         Nd = PgNode (PropGraph.NodeId, Type) 
         self.Id2Node [Nd.Id] = Nd

         PropGraph.NodeId += 1
         return Nd

    def AddEdge (self, Edge):
        self.EdgeList.append (Edge)


    def VisitAst(self, node):
        if node is None:
            return

        method = 'pg_' + node.__class__.__name__.lower()
        print (method)
        operator = getattr(self, method, self.generic_visit)        
        return operator(node)

    def pg_call(self, node):
        print (ast.dump (node.func), end="\n\n")
        if isinstance(node.func, Attribute):
            self.visit (node.func)
        else:
            pass
    
    def pg_functiondef (self, node):
        print (ast.dump (node), end="\n\n")
        for st in node.body:
            self.VisitAst (st)

    def pg_classdef(self, node):
        self.CurClass = node.name
        
        for st in node.body:
            self.VisitAst (st)
            
        self.CurClass = None
        
    def Build (self):
        print ("\r\n================ PropGraph.Build ================\r\n")
        for tmpt in ATs.TmptList:
            print (tmpt)
            astTmpt = ast.parse(tmpt)
            print (ast.dump (astTmpt), end="\n\n")
            
            self.VisitAst (astTmpt.body[0])

