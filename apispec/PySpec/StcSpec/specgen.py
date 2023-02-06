import os
import sys, getopt
import argparse
from pyspec import *


def InitArgument (parser):
    parser.add_argument('--version', action='version', version='specgen 1.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')
    grp.add_argument('-d', '--debug', action='store_true', help='generate python app')
    grp.add_argument('-c', '--check', action='store_true', help='check the apispec file')
    grp.add_argument('-e', '--expr', action='store_true', help='generate api expresion')
                     
    parser.add_argument('path', nargs='?', help='source dir or file to process')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')


def main():
    parser = argparse.ArgumentParser()
    InitArgument (parser)
    opts = parser.parse_args()

    if opts.debug:
        SetDebug (1)

    if opts.check:
        if opts.path is None:
            parser.error('please specify the apispec file!')
            
        apiCheck = ApiSpecCheck (opts.path)
        apiCheck.Check ()
    elif opts.expr:
        if opts.path is None:
            parser.error('please specify the apispec file!')
            
        AE = ApiExpr (opts.path)
        AE.GenExpr ()
    else:
        if opts.path is None:
            parser.error('please specify path for api spec generation!')
            
        apiGen = ApiSpecGen (opts.path)
        apiGen.GenSpec ()
    
    print ("Run successful.....")

if __name__ == "__main__":
   main()
