
import argparse
from fuzzwrap import *

def InitArgument (parser):
    parser.add_argument('--version', action='version', version='appgen 1.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')              
    parser.add_argument('filename', nargs='?', help='apispec file path')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')
    
def main():
    parser = argparse.ArgumentParser()
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')
    grp.add_argument('-s', '--silent', action='store_true', help='run in silent mode')

    InitArgument (parser)
    opts = parser.parse_args()

    if opts.filename is None:
        parser.error('please specify the script file!')
    
    Print = True
    if opts.silent == True:
        Print = False

    Ret = RunScript (opts.filename, Print)
    print (Ret)

if __name__ == "__main__":
   main()

