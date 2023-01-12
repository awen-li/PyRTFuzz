
# _*_ coding:utf-8 _*_
import os
import re
import ast
from ast import *
import astunparse

class PyApi ():
    def __init__ (self, ApiName, Expr, Ret, Args, PosArgs, KwoArgs, Defas, KwoDefas, Deps):
        self.ApiName = ApiName
        self.Expr    = Expr
        self.Ret     = Ret
        self.Args    = Args
        self.PosArgs = PosArgs
        self.KwoArgs = KwoArgs

        self.Defas = Defas
        self.KwoDefas = KwoDefas

        self.Deps = Deps
        
class PyCls ():
    def __init__ (self, clsName, Init):
        self.clsName = clsName
        self.clsInit = Init
        self.Apis = {}


class PyMod ():
    def __init__ (self, mdName):
        self.mdName  = mdName
        self.Apis    = {}
        self.Classes = {}

class PyExcep ():
    def __init__ (self, exName):
        self.exName  = exName

        
class PyLib ():
    def __init__ (self, Name):
        self.Name  = Name
        self.Modules = {}
        self.Exceptions = []

class AstWalk(NodeVisitor):
    def __init__(self):
        self.pyLibs  = []
        self.pyMods  = []

        self.CurPyLib = None
        self.CurPyMod = None
        self.CurClass = None
        self.CurFunc  = None
        
        self.FuncCalled  = {}
        self.FuncRetType = {}

        self.GetAttr = False

    def Reset (self):
        self.FuncCalled = {}
        self.FuncRetType = {}
        
    def SetPyLib (self, Name):
        self.CurPyLib = PyLib (Name)
        self.pyLibs.append (self.CurPyLib)

    def SetPyMod (self, Name):
        self.CurPyMod = PyMod (Name)
        if self.CurPyLib == None:
            self.pyMods.append (self.CurPyMod)
        else:
            self.CurPyLib.Modules [Name] = self.CurPyMod

    def GetFP (self, Args):
        ArgList = Args.args
        fp = []
        for arg in ArgList:
            if arg.arg == 'self':
                continue
            fp.append (arg.arg)

        PosArgs = Args.posonlyargs
        pa = [arg.arg for arg in PosArgs]
            
        KwArgs  = Args.kwonlyargs
        ka = [arg.arg for arg in KwArgs]

        Defaults = Args.defaults
        defa = [self.visit (val) for val in Defaults]

        KwDefaults = Args.kw_defaults
        kwdfa = [self.visit (val) for val in KwDefaults]
        
        return fp, pa, ka, defa, kwdfa

    def visit(self, node):
        """Visit a node."""
        if node is None:
            return
        method = 'visit_' + node.__class__.__name__.lower()
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def _IsInternal (self, FuncName):
        if FuncName == '__init__':
            return False
        
        if FuncName[0:1] == "_":
            return True
        else:
            return False

    def visit_unaryop (self, node):
        if isinstance (node.operand, Constant):
            return 'int'
        else:
            return None

    def visit_binop (self, node):
        if isinstance (node.left, Constant) or isinstance (node.right, Constant):
            return 'int'
        else:
            return None

    def visit_boolop(self, node):
        pass

    def visit_subscript(self, node):
        pass
  
    def visit_return (self, node):
        if node.value == None:
            return None
        
        if self.CurFunc == None:
            return None
        FuncName = self.CurFunc.ApiName

        Value = node.value
        if isinstance (Value, Tuple):
            pass
        else:
            ret = self.visit(node.value)
            if isinstance (ret, bool):
                ret = 'bool'
                
            if ret != None:
                if ret in ['int', 'float', 'string', 'bool']:               
                    RetType  = f'ret:{ret}'
                else:
                    RetType  = f'{ret}:None'
                
                if not RetType in self.CurFunc.Ret:
                    self.CurFunc.Ret.append (RetType)
                    self.FuncRetType [FuncName] = self.CurFunc.Ret
            else:
                self.CurFunc.Ret = ['ret:None']
                
        return None
        
    def visit_call (self, node):
        Callee = node.func
        if isinstance(Callee, Attribute):            
            self.FuncCalled[Callee.attr] = True
        elif isinstance(Callee, Name):
            self.FuncCalled[Callee.id] = True

        return self.visit (Callee)  

    def visit_for(self, node):
        for s in node.body:
            self.visit(s)

    def visit_while(self, node):
        for s in node.body:
            self.visit(s)

    def visit_if(self, node):
        for s in node.body:
            self.visit(s)

        for s in node.orelse:
            self.visit(s)

    def visit_with(self, node):
        for s in node.body:
            self.visit(s)

    def visit_constant (self, node):
        return node.value
        
    def visit_name (self, node):
        return node.id

    def visit_attribute (self, node, getstr=False):
        if self.GetAttr == False:
            return
        else:
            return self.visit (node.value) + '.' + node.attr
        
    def visit_try(self, node):
        for s in node.body:
            self.visit(s)

        for s in node.orelse:
            self.visit(s)

        for s in node.finalbody:
            self.visit(s)

        # handlers
        type_names_body = []
        for handler in node.handlers:
            type = handler.type
            if isinstance (type, Name):
                type_names_body.append(type.id)
            elif isinstance (type, Attribute):
                self.GetAttr = True
                type_names_body.append(self.visit_attribute (type))
                self.GetAttr = False
            else:
                print ("@@@@@@@@@@@@@@@ \r\n" + ast.dump (handler) + " ---> visit_try -> Unsuport type!!!")
                
        print (type_names_body)
    
    def visit_expr(self, node):
        self.visit (node.value)

    def visit_assign(self, node):
        for tgt in node.targets:
            self.visit (tgt)
        self.visit (node.value)

    def visit_augassign(self, node):
        self.visit (node.target)
        self.visit (node.value)

    def visit_annassign(self, node):
        for tgt in node.targets:
            self.visit (tgt)
        self.visit (node.value)

    def visit_asyncfunctiondef (self, node, ClfName=None):
        self.visit_functiondef (node, ClfName)
    
    def visit_functiondef(self, node, ClfName=None):

        if self.CurFunc != None:
            return

        ApiName = node.name
        if ApiName[0:4] == 'test':
            return

        if self._IsInternal (node.name) == True or isinstance (node.body[0], Pass):
            return
            
        fa, pa, ka, defas, kwdefas = self.GetFP (node.args)
        self.CurFunc = PyApi (ApiName, None, [], 
                              [p+':None' for p in fa], 
                              [p+':None' for p in pa], 
                              [p+':None' for p in ka],
                              defas, kwdefas,
                              None)

        if ApiName != '__init__':
            for stmt in node.body:
                self.visit (stmt)

        if self.CurClass != None:
            self.CurClass.Apis[ApiName] = self.CurFunc
        else:
            self.CurPyMod.Apis[ApiName] = self.CurFunc
        self.CurFunc = None

        return None

    def visit_classdef(self, node):

        clsname = node.name
        if self.CurClass != None:
            return 
            
        self.CurClass = PyCls (clsname, None)
        self.CurPyMod.Classes [clsname] = self.CurClass
        
        Body = node.body
        for Fdef in Body:
            if not isinstance (Fdef, FunctionDef):
                continue         
            self.visit_functiondef (Fdef, node.name)

        # check whether the function is invoked
        for api,_ in self.FuncCalled.items ():
            if self.CurClass.Apis.get (api) != None:
                self.CurClass.Apis.pop (api)

        self.CurClass = None
        return

    def visit_module(self, node):
        for s in node.body:
            self.visit(s)
        self.Reset ()
        