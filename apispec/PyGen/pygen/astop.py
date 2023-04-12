
import os
import ast
from ast import *
from .propgraph import *
from .debug import *
from platform import python_version

py_version = python_version()[0:3]

def EXPR2TYPE (Expr):
    Expr, TypeList = Expr.split('%%')
    return Expr, eval(TypeList)

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
    ApiTypeList = 'API_TYPE_LIST'
    ClsTypeList = 'CLS_TYPE_LIST'
    ArgDeCode   = 'PyDecode'

    def __init__(self, Tmpt, Main='RunFuzzer'):
        self.Tmpt   = Tmpt
        self.pG     = PropGraph ()
        self.RootPg = self.pG.Build (self.Tmpt)
        self.Main   = Main

    def GetWrapF (self):
        for root in self.RootPg:
            if root.Type == PropGraph.NodeType_CLASS:
                # properity G entry
                continue
            return self.pG.VisitGp (GetWrapF, root, PropGraph.EdgeType_CFG)
        return None

    def GetMainNode (self):
        for root in self.RootPg:
            if root.Name == self.Main:
                return root

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
    
    def op_new_import (self, NameList):
        return Import(names=[alias(name=N) for N in NameList])

    def op_new_constant (self, val):
        if py_version == "3.9":
            return Constant(value=val)
        elif py_version in ["3.8","3.7"]:
            return Constant(value=val, kind=None)
        else:
            raise Exception("Unsupported python version -> " + py_version)

    def op_new_load  (self, name):
        return Name(id=name, ctx=Load())

    def op_new_store (self, name):
        return Name(id=name, ctx=Store())

    def op_new_value (self, name):
        return self.op_new_load (name)

    def op_new_assignment (self, left, right):
        asgn = Assign(targets=[left], value=right)
        return asgn

    def op_new_try (self, stmts):
        return Try(body=stmts, handlers=[], orelse=[], finalbody=[])
    
    def op_new_raise (self, Excp):
        if py_version == "3.9":
            return Raise(exc=self.op_new_value (Excp))
        elif py_version in ["3.8","3.7"]:
            return Raise(exc=self.op_new_value (Excp), cause=None)
        else:
            raise Exception("Unsupported python version -> " + py_version)
        
    def op_new_tuple (self, list):
        return Tuple(elts=[self.op_new_value (i) for i in list])

    def op_new_const_list (self, list):
        return List(elts=[self.op_new_constant (i) for i in list], ctx=Load())

    def op_new_excep_handler (self, excepList):
        if len (excepList) == 0:
            return ExceptHandler ()
        else:
            excepTuple = self.op_new_tuple (excepList)
            return ExceptHandler(type=excepTuple, name='e')

    def op_new_attribute (self, name, attr):
        return Attribute(value=self.op_new_value (name), attr=attr, ctx=Load())

    def op_new_call (self, name, attr, args):
        call= None
        if attr == None:
            call = Call(func=self.op_new_value (name),
                         args=[self.op_new_value (arg) for arg in args],
                         keywords=[])
        else:
            call = Call(func=self.op_new_attribute (name, attr),
                         args=[self.op_new_value (arg) for arg in args],
                         keywords=[])
        return call
    
    def op_new_arg (self, x):
        if py_version == "3.9":
            return arg(arg=x)
        elif py_version in ["3.8", "3.7"]:
            return arg(arg=x, annotation=None)
        else:
            raise Exception("Unsupported python version -> " + py_version)

    def op_new_arguments (self, args):
        if py_version == "3.7":
            argmt= arguments(args=[self.op_new_arg(x) for x in args],
                            vararg=None,
                            kwonlyargs=[], kw_defaults=[], 
                            kwarg=None,
                            defaults=[])
        elif py_version == "3.8":
            argmt= arguments(posonlyargs=[],
                            args=[self.op_new_arg(x) for x in args],
                            vararg=None,
                            kwonlyargs=[], kw_defaults=[], 
                            kwarg=None,
                            defaults=[])
        elif py_version == "3.9":
            argmt= arguments(posonlyargs=[],
                            args=[self.op_new_arg(x) for x in args],
                            kwonlyargs=[], kw_defaults=[], defaults=[])
        else:
            raise Exception("Unsupported python version -> " + py_version)
        return argmt

        
    def op_new_functiondef (self, fname, args):
        funcdef = FunctionDef(name=fname,
                              args=self.op_new_arguments(args),
                              body=[],
                              decorator_list=[])
        return funcdef

    def op_new_expr (self, expr):
        return Expr(value=expr)

    def op_new_return (self, ret):
        return Return(value=ret)

    def op_new_argtypes (self, Name, TypeList):
        return Assign(targets=[self.op_new_store (Name)], value=self.op_new_const_list(TypeList))
        
    def op_value (self, node):
        return node

    def op_for (self, node):
        DebugPrint (ast.dump (node), end="\n\n")
        return node
    
    def op_return(self, node):
        return node
    
    def op_assign(self, node):
        DebugPrint (ast.dump (node), end="\n\n")

        for tg in node.targets:
            self.visit (tg)
        
        self.visit (node.value)
        return node

    def op_atrribute (self, node):
        return node

    def op_call(self, node):
        return node
    
    def op_try(self, node):
        return node

    def op_insert_invocation (self, node, InitStmt, CallStmt):
        if InitStmt != None:
            if self.IsBlankBody (node.body):
                node.body = InitStmt.body
            else:
                node.body += InitStmt.body
            node.body += CallStmt.body
        else:
            if self.IsBlankBody (node.body):
                node.body = CallStmt.body
            else:
                node.body += CallStmt.body
        return node

    def op_new_decoding (self, CallArgs, InFp):
        ArgName = [arg.id for arg in CallArgs]
        if len (ArgName) == 1:
            return Assign(targets=[self.op_new_store (arg) for arg in ArgName],
                          value=self.op_new_call (AstOp.ArgDeCode, None, InFp))
        else:
            return Assign(targets=[Tuple(elts=[self.op_new_store (arg) for arg in ArgName], ctx=Store())],
                          value=self.op_new_call (AstOp.ArgDeCode, None, InFp))

    def op_new_invoke_api (self, api, Fp):
        Expr, _ = EXPR2TYPE (api.Expr)
        CallStmt = ast.parse(Expr)
        if self.HasArgs (CallStmt.body[0]):
            DefStmt = self.op_new_decoding (CallStmt.body[0].value.args, [AstOp.ApiTypeList, Fp[0]])
            CallStmt.body = [DefStmt] + CallStmt.body

        # update the graph
        for Stmt in CallStmt.body:
            self.pG.pg_call (Stmt.value, self.criterion)      
        return CallStmt

    def op_new_invoke_constructor (self, init):
        if init != None:
            Init, _ = EXPR2TYPE (self.init)
            InitStmt = ast.parse(Init)
            return InitStmt
        else:
            return None
    
    def op_functiondef (self, node):
        if self.criterion == None:
            return node
        
        if node.name != self.criterion.Name:
            return node

        # get the FP of current node
        if self.criterion.NodeVal == None or self.criterion.NodeVal.Attr != NodeVal.NodeAttr_FP:
            raise Exception("Unspected value type!")
        fp = self.criterion.NodeVal.Val
        DebugPrint (self.criterion.Name + " formal paras: " + str(fp))

        # Obtain the ast for constructor of the API
        InitStmt = self.op_new_invoke_constructor (self.init)
        
        # Obtain the ast for invocation of the API
        CallStmt = self.op_new_invoke_api (self.api, fp)

        # encode new body
        node = self.op_insert_invocation (node, InitStmt, CallStmt)

        node.body = self.op_try_wrapper (node.body, self.excepts)
        
        return node

    def op_classdef(self, node):
        #DebugPrint (ast.dump (node), end="\n\n")
        for st in node.body:
            self.visit (st)
        return node
    
    def op_module(self, node):
        for st in node.body:
            self.visit(st)
        return node

    def op_try_wrapper (self, targetBody, targetExceps, Body=[Pass()]):
        IsExcepPass = os.getenv ("BYPASS_EXCEPTION")
        if IsExcepPass != None:
            targetExceps = ['Exception']

        #body=[Try(body=[Pass()], 
        #      handlers=[ExceptHandler(type=Tuple(elts=[Name(id='NameError', ctx=Load()), Name(id='TypeError', ctx=Load())], ctx=Load()), name='error', body=[Pass()])]
        tryStmt = self.op_new_try(targetBody)
        handler = self.op_new_excep_handler(targetExceps)
        handler.body = Body
        tryStmt.handlers.append (handler)

        return [tryStmt]

    def op_type_list (self, CurAst, ApiExpr, InitExpr):
        if ApiExpr != None:
            _, TypeList = EXPR2TYPE (ApiExpr)
            CurAst.body = [self.op_new_argtypes (AstOp.ApiTypeList, TypeList)] + CurAst.body

        if InitExpr != None:
            _, TypeList = EXPR2TYPE (InitExpr)
            CurAst.body = [self.op_new_argtypes (AstOp.ClsTypeList, TypeList)] + CurAst.body
        
        return CurAst

    def GenApp (self):
        print ("GenApp Default!")

