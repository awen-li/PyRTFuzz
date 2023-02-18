
# _*_ coding:utf-8 _*_
import random
import string
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

class PyInherit(AstOp):
    Tmpt =\
    """
class demoCls:
    def __init__(self):
        pass

    def demoFunc1(self, arg1):
        pass

def RunFuzzer (x):
    ob = demoCls ()
    ob.demoFunc1 (x)
    """
    
    def __init__(self):
        super(PyInherit, self).__init__(PyInherit.Tmpt)
        self.cls  = None
        self.init = None
        self.api  = None
        self.excepts   = None
        self.criterion = None
        self.ovfunc    = None
    
    def SetUp (self, init, api, excepts, cls=None):
        self.cls  = cls
        self.init = init
        self.api  = api
        self.excepts = excepts

        api.Expr = api.Expr.replace ('obj.', 'self.')

    def SetClass (self, pyClass):
        self.pyClass = pyClass
        print (self.pyClass)

    def op_new_base (self):
        if self.cls == None:
            raise Exception("op_base -> Unsupport without base class!!!")

        base = None
        cls = self.cls.split ('.')
        if len (cls) > 2:
            raise Exception("op_base -> Unsupport format " + self.cls)
        elif len (cls) == 2:
            base = self.op_new_attribute (cls[0], cls[1])
        else:
            base = self.op_new_value (cls[0])
    
        return [base]

    def op_insert_apiinvoke (self, node, InitStmt, CallStmt):
        if self.IsBlankBody (node.body):
            node.body = CallStmt.body
        else:
            node.body += CallStmt.body
        return node
        
    def op_functiondef (self, node):
        if self.ovfunc != None:
            if self.ovfunc.name == node.name:
                self.ovfunc = None
        return super ().op_functiondef (node)   
        
    def op_classdef(self, node):
        # add base
        node.bases = self.op_new_base ()

        # get all function def
        allFunctions = []
        for st in node.body:
            if isinstance (st, FunctionDef):
                allFunctions.append (st.name)
        print (allFunctions)       

        # override one function
        for apiName, api in self.pyClass.Apis.items ():        
            paras = [p.split(':')[0] for p in api.Args]
            self.ovfunc = self.op_new_functiondef (apiName, paras)
            if not self.ovfunc.name in allFunctions:
                # sp = super ()
                asgn = self.op_new_assignment (self.op_new_store ('sp'), self.op_new_call ('super', None, []))
                self.ovfunc.body.append (asgn)

                # sp.cur_func ()
                call = self.op_new_call ('sp', apiName, paras)
                if len (api.Ret) == 0:
                    expr = self.op_new_expr (call)
                    self.ovfunc.body.append (expr)
                else:
                    ret = self.op_new_return (call)
                    self.ovfunc.body.append (ret)
                
                node.body.append (self.ovfunc)
        return super ().op_classdef (node)

        
    def GenApp (self):
        self.criterion = self.GetWrapF ()
        if self.criterion == None:
            DebugPrint ("[GenApp] get the insert point fail!...")
            return
        self.criterion.View()
        DebugPrint ("GenApp -> api: " + str(self.init) + "  " + self.api.Expr)

        astApp = ast.parse(PyInherit.Tmpt)
        new = self.visit(astApp)

        # add api type list
        if self.api != None:
            TypeList = GetArgTypeList (self.api)
            new.body = [self.op_new_argtypes (TypeList)] + new.body
            
        DebugPrint (astunparse.unparse(new))
        self.pG.ShowPg ()
        return astunparse.unparse(new)

        
        

        