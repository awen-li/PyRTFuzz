import os
import sys, getopt
import argparse
from pygen import *


def InitArgument (parser):
    parser.add_argument('--version', action='version', version='appgen 1.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')
    grp.add_argument('-g', '--generate', action='store_true', help='generate python app')
    grp.add_argument('-d', '--debug', action='store_true', help='generate python app')
                     
    parser.add_argument('filename', nargs='?', help='apispec file path')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')


def main():
    parser = argparse.ArgumentParser()
    InitArgument (parser)
    opts = parser.parse_args()

    if opts.debug:
        SetDebug (1)

    if opts.generate:
        if opts.filename is None:
            parser.error('please specify the apispec file!')
        
        SG = CodeGen (opts.filename)
        SG.GenPy ('xyz', 2)

        print ("Run successful.....")
    else:
        print ("Do nothing?")

if __name__ == "__main__":
   main()
