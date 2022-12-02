
import os
import sys, getopt
import argparse
import time
import ast
from ast import *
import astunparse

source_def = \
"""
import io
import pickle

class Pickler(pickle.Pickler):
  def persistent_id(self, obj):
    return super().persistent_id(obj)

Pickler(io.BytesIO()).dump(42)

"""

def NewClass (Name):
    Template = \
f"""
class {Name}:
    def __init__(self):
        pass
"""
    return Template

def NewFunc ():
    pass


def NewExpr ():
    pass


def DemoGen ():
    AstTree = ast.parse(source_def)

    AstStr = ast.dump(AstTree)
    print (AstStr)
    
    Source = astunparse.unparse(AstTree)
    print (Source)

    NewCls = NewClass ("HelloWorld")
    print (NewCls)


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

    DemoGen ()

    print ("Run successful.....")

if __name__ == "__main__":
   main()
