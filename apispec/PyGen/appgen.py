import os
import sys, getopt
import argparse
from pygen import *


def InitArgument (parser):
    parser.add_argument('--version', action='version', version='appgen 1.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')
    grp.add_argument('-g', '--generate', action='store_true', help='generate python app')
    grp.add_argument('-d', '--debug', action='store_true', help='generate python app')
    grp.add_argument('-s', '--show', action='store_true', help='show all supported CMDs')
    grp.add_argument('-a', '--api', help='target api for app generation')
    grp.add_argument('-l', '--length', help='length of SL script')
                     
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

        if opts.api is None:
            parser.error('please specify the api!')
        
        SG = CodeGen (opts.filename)

        if opts.length is None:
            SG.GenPyApp (opts.api)
        else:
            SG.GenPyApp (opts.api, StateNum=int(opts.length))

        print ("Run successful.....")
    elif opts.show:
        Core ().ShowCmds ()
    else:
        print ("Do nothing?")

if __name__ == "__main__":
   main()
