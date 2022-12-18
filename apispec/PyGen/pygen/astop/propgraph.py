
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

class NodeValue ():
    NodeAttr_None = 0
    NodeAttr_FP   = 1
    NodeAttr_AP   = 2
    
    def __init__ (self, Attr=0):
        self.Attr = Attr


class NV_fp (NodeValue):
    def __init__ (self, FP):
        super(NV_fp, self).__init__(NodeValue.NodeAttr_FP)
        self.FP = FP

class PgNode ():
    def __init__ (self, Id, Type, Name='node'):
        self.Id   = Id
        self.Name = Name
        self.NodeVal = None
        
        self.InEdge  = []
        self.OutEdge = []


class PgEdge ():
    def __init__ (self, Src, Dst, Type):
        self.SrcNd = Src
        self.DstNd = Dst
        self.Type  = Type

        
class PropGraph (NodeVisitor):

    NodeId = 1

    NodeType_CLASS =1
    NodeType_FUNC  =2

    EdgeType_PROP = 1
    EdgeType_CFG  = 2
    EdgeType_DD   = 3
    
    def __init__ (self, MainFunc='RunFuzz'):
        self.MainFunc = MainFunc
        self.FuncList = {}
        self.Id2Node  = {}
        self.EdgeList = []

        self.CurClass = None
        self.CurFunc  = None

    def GetFP (self, Args):
        ArgList = Args.args
        fp = []
        for arg in ArgList:
            if arg.arg == 'self':
                continue
            fp.append (arg.arg)
        return NV_fp (fp)

    def GetAP (self):
        pass

    def AddNode (self, Type, Name='node'):
         Nd = PgNode (PropGraph.NodeId, Type, Name) 
         self.Id2Node [Nd.Id] = Nd

         PropGraph.NodeId += 1
         return Nd

    def AddEdge (self, Edge):
        self.EdgeList.append (Edge)


    def VisitAst(self, node):
        if node is None:
            return

        method = 'pg_' + node.__class__.__name__.lower()
        operator = getattr(self, method, self.generic_visit)        
        return operator(node)

    def pg_call(self, node):   
        print (self.CurFunc.Name, end="\n\n")
        if isinstance(node.func, Attribute):
            self.visit (node.func)
        else:
            pass
    
    def pg_functiondef (self, node):
        print (ast.dump (node), end="\n\n")
        FP = self.GetFP(node.args)
        self.CurFunc = self.AddNode (PropGraph.NodeType_FUNC, node.name)
        self.CurFunc.NodeVal = FP

        if self.CurClass != None:
            eg = PgEdge (self.CurClass, self.CurFunc, PropGraph.EdgeType_PROP)
            self.AddEdge (eg)
        
        for st in node.body:
            self.VisitAst (st)

        self.CurFunc = None

    def pg_classdef(self, node):
        Nd = self.AddNode (PropGraph.NodeType_CLASS, node.name)
        self.CurClass = Nd
        
        for st in node.body:
            self.VisitAst (st)
            
        self.CurClass = None
        
    def Build (self):
        print ("\r\n================ PropGraph.Build ================\r\n")
        for tmpt in ATs.TmptList:
            print (tmpt)
            astTmpt = ast.parse(tmpt)
            print (ast.dump (astTmpt), end="\n\n")

            for body in astTmpt.body:
                self.VisitAst (body)

