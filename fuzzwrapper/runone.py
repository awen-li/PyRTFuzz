
import os
import sys
import argparse
import importlib

def InitArgument (parser):
    parser.add_argument('--version', action='version', version='appgen 1.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')              
    parser.add_argument('filename', nargs='?', help='apispec file path')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')

def RunScript (script):

    absPath  = os.path.abspath (script)
    absDir   = os.path.dirname (absPath)
    baseName = os.path.basename (script)
    print ("@@@ PyCoreFuzz -> " + absDir + "  --->  " + baseName)

    if absDir not in sys.path:
        sys.path.insert(0, absDir)

    md  = baseName.split('.')[0]
    lib = importlib.import_module(md)
    
    lib.RunFuzzer ('0')

    
def main():
    parser = argparse.ArgumentParser()
    InitArgument (parser)
    opts = parser.parse_args()


    if opts.filename is None:
        parser.error('please specify the script file!')

    RunScript (opts.filename)

if __name__ == "__main__":
   main()

