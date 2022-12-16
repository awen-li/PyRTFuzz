
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
    def __init__ (self,Id, Type):
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
        self.Id2Node  = {}
        self.EdgeList = []

    def AddNode (self, Type):
         Nd = PgNode (PropGraph.NodeId, Type) 
         self.Id2Node [Nd.Id] = Nd

         PropGraph.NodeId += 1
         return Nd

    def AddEdge (self, Edge):
        self.EdgeList.append (Edge)


    def Build (self):
        for tmpt in ATs.TmptList:
            print (tmpt)

