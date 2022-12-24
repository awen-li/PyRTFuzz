
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
class demoCls:
    def __init__(self):
        pass

    def demoFunc0(self):
        pass

    def demoFunc1(self, PYF_ARG1):
        pass

def RunFuzzer (x):
    pass
"""

pg_tempt_pro = \
"""
def demoFunc0 ():
    pass

def demoFunc1 (PYF_ARG1):
    pass

def RunFuzzer (x):
    pass
"""

pg_for = \
"""
for PYF_I in range (0, PYF_E):
    pass
"""

pg_inherit = \
"""
import io
import pickle

class Pickler(pickle.Pickler):
  def persistent_id(self, obj):
    return super().persistent_id(obj)

Pickler(io.BytesIO()).dump(42)
"""


Instance2Ast = {}

if not os.path.exists ('pickle_set'):
    os.mkdir ('pickle_set')

def WriteAstPickle (Name, Ast):
    PklFile = 'pickle_set/' + Name + ".pkl"
    with open(PklFile, 'wb') as Pkl:
        pickle.dump(Ast, Pkl)
    Instance2Ast[Name] = PklFile
    print ("Write pickle of %s to %s" %(Name, PklFile))
    #print (ast.dump (Ast))

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

    Ast = ast.parse(pg_for)
    WriteAstPickle ('pg_for', Ast)


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
    
    Ast = ast.parse(pg_tempt_oo)
    print ("=============   original source   =============\r\n")
    print (astunparse.unparse(Ast))
    
    FuncAst = ast.parse (ApiSpecInfo ['cmath.exp'].Expr)
    
    CO = ClassOp ("demoCls", FuncAst, 'INSERT_CALL')
    NewAst = CO.visit (Ast)
    FO = FuncOp ('RunFuzzer', ast.parse('demoCls ().demoFunc1(x)'), 'INSERT_ENTRY')
    NewAst = FO.visit (NewAst)
    print ("=============   after op-CLASS-INSERT_CALL   =============\r\n")
    print (astunparse.unparse(NewAst))

    uAst = ast.parse(pg_for)
    FO = FuncOp ('demoFunc1', uAst, 'INSERT_FOR')
    NewAst = FO.visit (NewAst)
    print ("=============   after op-FUNC-INSERT_FOR   =============\r\n")
    print (astunparse.unparse(NewAst))




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
