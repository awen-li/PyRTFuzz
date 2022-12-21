
import ast
from ast import *

"""
Example:
class demoCls:
    def __init__(self):
        pass

    def demoFunc1(self, arg1):
        pass

def RunFuzzer (x):
    dc = demoCls ()
    dc.demoFunc1 (x)

-------------------------------------------------------------------
control flow graph:

               RunFuzzer (x)
                    |
          dc = demoCls.__init__()
                    |
             dc.demoFunc1 (x)

class graph:
                demoCls
                /     \
  __init__ (init)    demoFunc1 (x)
"""

class NodeVal ():
    NodeAttr_None = 0
    NodeAttr_FP   = 1
    NodeAttr_AP   = 2
    
    def __init__ (self, Val, Attr=0):
        self.Val  = Val
        self.Attr = Attr

    def View (self):
        Types = ['None', 'FP', 'AP']
        print (str(self.Val) + ' ---> with type: ' + Types[self.Attr])

class PgNode ():
    def __init__ (self, Id, Type, Name='node'):
        self.Id   = Id
        self.Type = Type
        self.Name = Name
        self.NodeVal = None
        
        self.InEdge  = []
        self.OutEdge = []

    def AddInEdge (self, InEg):
        self.InEdge.append (InEg)

    def AddOutEdge (self, OutEg):
        self.OutEdge.append (OutEg)


class PgEdge ():
    def __init__ (self, Src, Dst, Type, Val=None):
        self.SrcNd = Src
        self.DstNd = Dst
        self.Type  = Type
        self.Val   = Val

        
class PropGraph (NodeVisitor):

    NodeType_CLASS = 1
    NodeType_FUNC  = 2
    NodeType_STMT  = 3
    NodeTypes = ['NONE', 'CLASS', 'FUNCTION', 'STATEMENT']

    EdgeType_PROP = 1
    EdgeType_CFG  = 2
    EdgeType_DD   = 3
    EdgeType_CALL = 4
    EdgeTypes = ['NONE', 'PROPERITY', 'CFG', 'DD', 'CALL']
    
    def __init__ (self, MainFunc='RunFuzz'):
        self.NodeId   = 1
        self.MainFunc = MainFunc
        
        self.Id2Node  = {}
        self.EdgeList = []

        self.CurClass = None
        self.CurFunc  = None

        self.FuncList = {}
        self.ClsList  = {}

    def VisitGp (self, Hook, Root, Type=None):
        N = Root
        Res = None
        
        queue = []
        queue.append (N)
        while len (queue) != 0:
            N = queue.pop (0)
            
            Res = Hook (N)
            if Res != None:
                return Res
   
            for oe in N.OutEdge:
                if Type == None or oe.Type == Type:
                    queue.append (oe.DstNd)
        return None

    def AddFunc (self):
        Cls = ''
        if self.CurClass != None:
            Cls = self.CurClass.Name + '.'

        FuncName = Cls + self.CurFunc.Name
        self.FuncList [FuncName] = self.CurFunc

    def GetFunc (self, FuncName):
        Def = self.FuncList.get (FuncName)
        if Def == None:
            for clsName, clsNd in self.ClsList.items ():
                for oe in clsNd.OutEdge:
                    if oe.Type != PropGraph.EdgeType_PROP:
                        continue
                    dst = oe.DstNd
                    if dst.Name == FuncName:
                        return dst
        return None                    
     
    def GetFP (self, Args):
        ArgList = Args.args
        fp = []
        for arg in ArgList:
            if arg.arg == 'self':
                continue
            fp.append (arg.arg)
        return NodeVal (fp, NodeVal.NodeAttr_FP)

    def GetAP (self, Args):
        ArgList = Args
        ap = []
        for arg in ArgList:
            if isinstance (arg, Name):
                ap.append (arg.id)
            else:
                raise Exception("GetAP -> Unsupport!!!")
            
        return NodeVal (ap, NodeVal.NodeAttr_AP)

    def GetId (self, name):
        return name.id

    def AddNode (self, Type, Name='node'):
         Nd = PgNode (self.NodeId, Type, Name) 
         self.Id2Node [Nd.Id] = Nd

         self.NodeId += 1
         return Nd

    def AddEdge (self, Edge):
        self.EdgeList.append (Edge)
        Src = Edge.SrcNd
        Dst = Edge.DstNd
        Src.AddOutEdge (Edge)
        Dst.AddInEdge (Edge)

    def IsDD (self, ApVal):
        FpList = self.CurFunc.NodeVal.Val
        for ap in ApVal.Val:
            if ap in FpList:
                return ap
        return None

    def VisitAst(self, node):
        if node is None:
            return

        method = 'pg_' + node.__class__.__name__.lower()
        operator = getattr(self, method, self.generic_visit)        
        return operator(node)

    def pg_assign(self, node):
        lefts = node.targets
        right = node.value
        self.VisitAst (right)    

    def pg_expr(self, node):   
        #print (ast.dump (node), end="\n\n")
        self.VisitAst (node.value)
        
    def pg_call(self, node):
        #print (ast.dump (node), end="\n\n")
        callee = None
        DefFunc = None
        
        ap = self.GetAP(node.args)
        #ap.View ()
        
        if isinstance(node.func, Attribute):            
            callee = self.GetId (node.func.value) + '.' + node.func.attr
            DefFunc = self.GetFunc(node.func.attr)
        elif isinstance(node.func, Name):
            callee = self.GetId (node.func)
            DefFunc = self.GetFunc(callee)
        else:
            raise Exception("pg_call -> Unsupport!!!")

        CalleeNd = self.AddNode (PropGraph.NodeType_STMT, callee)
        CalleeNd.NodeVal = ap

        #Call  
        if DefFunc != None:
            eg = PgEdge (CalleeNd, DefFunc, PropGraph.EdgeType_CALL)
            self.AddEdge (eg)

        
        # add a CFG edge
        eg = PgEdge (self.CurFunc, CalleeNd, PropGraph.EdgeType_CFG)
        self.AddEdge (eg)

        # check DDG from FP
        ddAp = self.IsDD (ap)
        if ddAp != None:
            ddEg = PgEdge (self.CurFunc, CalleeNd, PropGraph.EdgeType_DD, ddAp)
            self.AddEdge (ddEg)
    
    def pg_functiondef (self, node):
        #print (ast.dump (node), end="\n\n")
        fp = self.GetFP(node.args)
        #fp.View ()
        
        self.CurFunc = self.AddNode (PropGraph.NodeType_FUNC, node.name)
        self.CurFunc.NodeVal = fp
        self.AddFunc ()

        if self.CurClass != None:
            eg = PgEdge (self.CurClass, self.CurFunc, PropGraph.EdgeType_PROP)
            self.AddEdge (eg)
        
        for st in node.body:
            self.VisitAst (st)
        
        self.CurFunc = None

    def pg_classdef(self, node):
        Nd = self.AddNode (PropGraph.NodeType_CLASS, node.name)
        self.CurClass = Nd
        self.ClsList [node.name] = Nd
        
        for st in node.body:
            self.VisitAst (st)
            
        self.CurClass = None

    def GetRoots (self):
        root = []
        for id, node in self.Id2Node.items ():
            if len (node.InEdge) == 0:
                root.append (node)
        return root
        

    def ShowPg (self):
        # get roots
        root = self.GetRoots ()
        
        print ("\r\nNode List:")
        for id, node in self.Id2Node.items ():
            print ("[%d]%s" %(node.Id, node.Name))

        print ("\r\n")
        # iter root
        for r in root:
            queue = []
            print ("\r\n[%s][%d]Root: %s" %(PropGraph.NodeTypes[r.Type], r.Id, r.Name))
            queue.append (r)
            while len (queue) != 0:
                curNode = queue.pop (0)
                
                for oe in curNode.OutEdge:
                    print ("\t [%d, %d](%s)" %(oe.SrcNd.Id, oe.DstNd.Id, PropGraph.EdgeTypes[oe.Type]), end='')
                    if  oe.Val != None:
                        print (str(oe.Val))
                    queue.append (oe.DstNd)
    
    def Build (self, App):
        print ("\r\n================ PropGraph.Build ================")
        print ("Template: \r\n" + App)
        astApp = ast.parse(App)
        for body in astApp.body:
            self.VisitAst (body)

        self.ShowPg ()
        return self.GetRoots ()

