
# _*_ coding:utf-8 _*_
import os
import re
import ast
from ast import *
import astunparse

class PyApi ():
    def __init__ (self, ApiName, Expr, Ret, Parameters, Dependences):
        self.ApiName = ApiName
        self.Expr    = Expr
        self.Ret     = Ret
        self.Parameters = Parameters
        self.Dependences = Dependences
        
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
        self.Imports = []
        self.pyLibs  = []
        self.pyMods  = []

        self.CurPyLib = None
        self.CurPyMod = None
        self.CurClass = None
        self.CurFunc  = None
        self.FuncCalled = []

    def SetPyLib (self, Name):
        self.CurPyLib = PyLib (Name)
        self.pyLibs.append (self.CurPyLib)

    def SetPyMod (self, Name):
        self.CurPyMod = PyMod (Name)
        self.pyMods.append (self.CurPyMod)

    def GetFP (self, Args):
        ArgList = Args.args
        fp = []
        for arg in ArgList:
            if arg.arg == 'self':
                continue
            fp.append (arg.arg)
        return fp

    def visit(self, node):
        """Visit a node."""
        if node is None:
            return
        method = 'visit_' + node.__class__.__name__.lower()
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def _IsInternal (self, FuncName):
        if FuncName[0:2] == "__":
            return True
        else:
            return False

    def visit_return (self, node):
        print ("IN function: " + self.CurFunc.ApiName + "  --->  " + ast.dump (node))
        
    def visit_call (self, node):
        Callee = node.func
        self.FuncCalled.append (Callee)
        

    def visit_functiondef(self, node, ClfName=None):
        if self._IsInternal (node.name) == True:
            return

        ApiName = node.name
        Parameters = self.GetFP (node.args)

        self.CurFunc = PyApi (ApiName, None, None, Parameters, None)
        for stmt in node.body:
            self.visit (stmt)

        if self.CurClass != None:
            self.CurClass.Apis[ApiName] = self.CurFunc
        else:
            self.CurMod.Apis[ApiName] = self.CurFunc
        self.CurFunc = None

        return

    def visit_classdef(self, node):

        clsname = node.name
        self.CurClass = PyCls (clsname, None)
        
        print ("visit class -> " + clsname)   
        
        Body = node.body
        for Fdef in Body:
            if not isinstance (Fdef, FunctionDef):
                continue         
            self.visit_functiondef (Fdef, node.name)

        self.CurClass = None
        return

    