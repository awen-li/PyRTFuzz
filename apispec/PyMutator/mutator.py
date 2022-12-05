
import os
import sys, getopt
import argparse
import pickle
import ast
from ast import *
import astunparse
from astwrite import *


pg_tempt_oo = \
"""
class PYF_CLASS:
    def __init__(self):
        pass

def RunFuzzer ():
    pass
"""

pg_tempt_pro = \
"""
def PYF_FUNCTION ():
    pass

def RunFuzzer ():
    pass
"""



Instance2Ast = {}

if not os.path.exists ('pickle_set'):
    os.mkdir ('pickle_set')

def WriteAstPickle (Name, Data):
    PklFile = 'pickle_set/' + Name + ".pkl"
    with open(PklFile, 'wb') as Pkl:
        pickle.dump(Data, Pkl)
    Instance2Ast[Name] = PklFile
    print ("Write pickle of %s to %s" %(Name, PklFile))

def LoadAstPickle (Name):
    PklFile = 'pickle_set/' + Name + ".pkl"
    with open(PklFile, 'rb') as Pkl:
        return pickle.load(Pkl)

def Prepare ():
    Ast = ast.parse("import PYF_IMPORT")
    WriteAstPickle ('import', Ast)

    Ast = ast.parse(pg_tempt_oo)
    WriteAstPickle ('pg_tempt_oo', Ast)

    Ast = ast.parse(pg_tempt_pro)
    WriteAstPickle ('pg_tempt_pro', Ast)

def NewClass (Name):
    Template = \
f"""
class {Name}:
    def __init__(self):
        pass

def RunFuzzer ():
    pass
"""
    return Template

def NewFunc ():
    pass


def NewExpr ():
    pass


class ApiSpec ():
    def __init__ (self, Module, ApiName, Expr):
        self.Module  = Module
        self.ApiName = ApiName
        self.Expr    = Expr
        self.Ret     = {}
        self.Parameters = []



ApiSpecInfo = {}

def InitApiSpec ():
    # demo for cmath.exp 
    cmath_exp = ApiSpec ('cmath', 'exp', 'ret = cmath.exp(x)')
    cmath_exp.Parameters = [{'x':type(0)}]
    cmath_exp.Ret  = {'ret':type(0)}
    ApiSpecInfo ['cmath.exp'] = cmath_exp



#####################################################################################################
#####################################################################################################
source_def = \
"""
import io
import pickle

class Pickler(pickle.Pickler):
  def persistent_id(self, obj):
    return super().persistent_id(obj)

Pickler(io.BytesIO()).dump(42)

"""

def DemoGen ():
    InitApiSpec ()
    
    AstTree = ast.parse(source_def)

    AstStr = ast.dump(AstTree)
    print (AstStr)
    
    Source = astunparse.unparse(AstTree)
    print (Source)

    NewCls = NewClass ("HelloWorld")
    print (NewCls)

    FuncAst = ast.parse (ApiSpecInfo ['cmath.exp'].Expr)
    print (ast.dump (FuncAst))
    
    Ast = ast.parse(pg_tempt_oo)
    CO = ClassOp ("PYF_CLASS", FuncAst)
    CO.visit (Ast)


def InitArgument (parser):
    parser.add_argument('--version', action='version', version='trace 2.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')                    
    parser.add_argument('dirname', nargs='?', help='source dir to process')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')


def main():
    parser = argparse.ArgumentParser()
    InitArgument (parser)

    opts = parser.parse_args()
    if opts.dirname is None:
        #parser.error('dirname is missing: required with the main options')
        pass

    Prepare ()
    DemoGen ()

    print ("Run successful.....")

if __name__ == "__main__":
   main()
