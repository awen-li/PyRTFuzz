
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
    grp.add_argument('-i', '--input', help='input for the script')

    InitArgument (parser)
    opts = parser.parse_args()

    if opts.filename is None:
        parser.error('please specify the script file!')
    
    Silent = True
    if opts.silent == True:
        Silent = False
    
    if opts.input != None:
        Inputs = opts.input
        if os.path.isfile(opts.input):
            with open (opts.input, 'r') as F:
                Inputs = F.read ()
        Ret = RunScript (opts.filename, Input=Inputs, Print=Silent)
    else:
        Ret = RunScript (opts.filename, Print=Silent)
    print (Ret)

if __name__ == "__main__":
   main()

