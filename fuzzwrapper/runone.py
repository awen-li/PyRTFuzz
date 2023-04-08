
import argparse
from fuzzwrap import *
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', help='the filename for running')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')

    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')
    grp.add_argument('-s', '--silent', action='store_true', help='run in silent mode')
    grp.add_argument('-i', '--input', help='input for the script')

    opts = parser.parse_args()

    if opts.filename is None:
        parser.error('please specify the script file!')
    
    Silent = True
    if opts.silent == True:
        Silent = False
    
    if opts.input != None:
        Inputs = opts.input
        if os.path.isfile(opts.input):
            with open (opts.input, 'rb') as F:
                Inputs = F.read ()
        Ret = RunScript (opts.filename, Input=Inputs, Print=Silent)
    else:
        Ret = RunScript (opts.filename, Print=Silent)
    print (Ret)

if __name__ == "__main__":
   main()

