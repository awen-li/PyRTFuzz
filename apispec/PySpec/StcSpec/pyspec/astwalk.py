
# _*_ coding:utf-8 _*_
import os
import re
import ast
from ast import *
import astunparse
from .apispec import *
from .utils import RunCmd, WriteValidate
from .validate import Path2Imports, ValidatedApiList, Class2Bases

IsDebug = os.environ.get ("PYDEBUG")

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

        PosArgs = []
        if hasattr(Args, "posonlyargs"):
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
    
    def GetRelativePath (self, ModPath):
        Index = ModPath.rfind ('.')
        if Index == -1:
            return None
        else:
            RelPath = ModPath[0:Index]
            return RelPath
        
    #ImportFrom(module='enum', names=[alias(name='Enum')], level=0)
    def visit_importfrom (self, node):
        #print (ast.dump(node))
        Module = node.module
        if Module == None:
            Module = self.GetRelativePath (self.CurPyMod.Name)
            if Module == None:
                return
        
        if Module[0:1] == '_':
            return
                
        Names = node.names
        for al in Names:
            if al.name[0:1] == '_':
                continue
            Ifm = Module+':'+al.name
            if not Ifm in self.CurPyMod.ImportFrom:
                self.CurPyMod.ImportFrom.append (Ifm)
        #print (self.CurPyMod.ImportFrom)

    #Import(names=[alias(name='io'), alias(name='os'), alias(name='shutil'), alias(name='subprocess')])
    def visit_import (self, node):
        #print (ast.dump (node))
        Names = node.names
        for al in Names:
            if al.name[0:1] == '_':
                continue
            if al.name in self.CurPyMod.Imports:
                continue
            if al.asname == None:
                self.CurPyMod.Imports.append (al.name)
            else:
                self.CurPyMod.Imports.append (al.name + ':' + str(al.asname))
        #print (self.CurPyMod.Imports)
    
    def IsSelfDef (self, Exc):
        for claname, cls in self.CurPyMod.Classes.items ():
            if Exc == claname:
                return True
        return False

    def visit_raise(self, node):
        Prefix = ''
        RaiseExpr = astunparse.unparse (node)
        Exc = re.findall (r'raise (.+?)\(', RaiseExpr)
        if len(Exc) != 0:
            if self.IsSelfDef (Exc[0]) == True:
                Prefix = self.CurPyMod.Name + '.'
            Excep = PyExcep (Prefix + Exc[0])
            self.AddExcep (Excep)
        else:
            Exc = re.findall (r'raise (.+?)$', RaiseExpr)
            if len(Exc) != 0:
                if self.IsSelfDef (Exc[0]) == True:
                    Prefix = self.CurPyMod.Name + '.'
                Excep = PyExcep (Prefix + Exc[0])
                self.AddExcep (Excep)
            else:
                print (RaiseExpr + ' --> ' + str(Exc))
    
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

    def AddExcep (self, Excep):
        self.CurPyMod.Exceptions.append (Excep)
        
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
            elif isinstance (type, Tuple):
                for elmt in type.elts:
                    if isinstance (elmt, Name):
                        type_names_body.append (elmt.id)
                    elif isinstance (type, Attribute):
                        self.GetAttr = True
                        type_names_body.append(self.visit_attribute (elmt))
                        self.GetAttr = False
                    else:
                        if IsDebug:
                            print ("@@@@@@@@@@@@@@@ \r\n" + ast.dump (elmt) + " ---> visit_try-Tuple -> Unsuport type!!!")
            else:
                if IsDebug:
                    print ("@@@@@@@@@@@@@@@ \r\n" + ast.dump (handler) + " ---> visit_try -> Unsuport type!!!")

        for excep in type_names_body:
            Prefix = ''
            if self.IsSelfDef (excep):
                Prefix = self.CurPyMod.Name + '.'
            Excep = PyExcep (Prefix+excep)
            self.AddExcep (Excep)
            
    
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
        self.visit (node.target)
        self.visit (node.value)

    def visit_asyncfunctiondef (self, node, ClfName=None):
        self.visit_functiondef (node, ClfName)
    
    def visit_functiondef(self, node, ClfName=None):

        if self.CurFunc != None:
            return

        ApiName = node.name
        if ApiName[0:4] == 'test':
            return

        if isinstance (node.body[0], Pass):
            return

        if IsDebug:
            print ("### function -> " + node.name)  
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
    
    def GetBases (self, clfNode):
        clfBase = clfNode.bases
        if len (clfBase) == 0:
            return []
        
        Bases = []
        for base in clfBase:
            if isinstance (base, Name):
                Bases.append(base.id)
            elif isinstance (base, Attribute):
                self.GetAttr = True
                bName = self.visit_attribute (base)
                self.GetAttr = False
                Bases.append (bName)
            elif isinstance (base, Subscript):
                Bases.append(base.value.id)
            else:
                if IsDebug:
                    print ("@@@@@@@@@@@@@@@ \r\n" + ast.dump (clfNode) + " ---> HandleErrInHerit -> Unsuport type!!!")

        return Bases

    def HandleErrInHerit (self, Bases, clsName):
        WholePath = self.CurPyMod.Name + '.' + clsName
        for bs in Bases:
            if bs.find ('Error') != -1 or bs.find ('Exception') != -1:
                Excep = PyExcep (WholePath)
                self.AddExcep (Excep)
                return True
            else:
                continue
        
        BaseInfo = Class2Bases.get (WholePath)
        if BaseInfo == None:
            Connector = '.'
            Cmd = f'python -c \'import {self.CurPyMod.Name},inspect; print ([[tn.__module__,tn.__name__] for tn in inspect.getmro({WholePath})])\''
            BaseInfo = RunCmd (Cmd)
            if BaseInfo == '' or BaseInfo.find ('Error: ') != -1:
                return False
                   
            BaseInfo = eval (BaseInfo)[1:]
            BaseInfo = ','.join('.'.join(BList) for BList in BaseInfo)
            Class2Bases [WholePath] = BaseInfo
                
        if BaseInfo.find ('Error') != -1 or BaseInfo.find ('Exception') != -1:
            Excep = PyExcep (WholePath)
            self.AddExcep (Excep)
            return True
        return False
    
    # ret0: bases, ret1: flag for exc inherit
    def HandleHerit (self, clfNode):
        Bases = self.GetBases (clfNode)
        if len(Bases) == 0:
            return None, False
        
        # check if inherit from error:
        if self.HandleErrInHerit (Bases, clfNode.name) == True:
            return Bases[0], True
        
        # update the base with absolute path
        CurBase = Bases[0]
        BaseInfo = Class2Bases.get (self.CurPyMod.Name + '.' + clfNode.name)
        if BaseInfo != None and BaseInfo[0:1] != '_':
            BaseInfo = BaseInfo.split (',')
            #print (CurBase + "  ---> " + BaseInfo[0])
            CurBase  = BaseInfo[0]
        
        return CurBase, False

    def visit_classdef(self, node):
        if self.CurClass != None or self.CurFunc != None:
            return

        Bases, IsErr = self.HandleHerit (node)

        clsname = node.name
        self.CurClass = PyCls (clsname, None, Bases)
        self.CurPyMod.Classes [clsname] = self.CurClass

        if IsErr == True:
            self.CurClass = None
            return
        
        Body = node.body
        for stmt in Body:
            if isinstance (stmt, FunctionDef):   
                self.visit_functiondef (stmt, node.name)
            else:
                self.visit (stmt)

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
        WriteValidate (Path2Imports, ValidatedApiList, Class2Bases)
        