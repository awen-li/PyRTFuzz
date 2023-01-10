
import os
import sys, getopt
import argparse
from pytrace import *


def InitArgument (parser):
    parser.add_argument('--version', action='version', version='trace 2.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')
    grp.add_argument('-s', '--source',
                     help='source api spec xml')
    grp.add_argument('-i', '--include_path',
                     help='the installation path of the target')
              
    parser.add_argument('filename', nargs='?', help='file to run as main program')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')

def DynTrace (EntryScript, ApiSpecXml):
    try:
        with open(EntryScript) as fp:
            code = compile(fp.read(), EntryScript, 'exec')

        globs = {
            '__file__': EntryScript,
            '__name__': '__main__',
            '__package__': None,
            '__cached__': None,
        }
        
        with Tracing (ApiSpecXml):
            exec(code, globs, globs)
        
    except OSError as err:
        sys.exit("Cannot run file %r because: %s" % (sys.argv[0], err))
    except SystemExit:
        sys.exit("except SystemExit")


def main():
    parser = argparse.ArgumentParser()
    InitArgument (parser)

    opts = parser.parse_args() 
    sys.argv = [opts.filename, *opts.arguments]

    if opts.filename is None:
        parser.error('filename is missing: required with the main options')
        
    if opts.source is None:
        #parser.error('please specify the original api spec xml')
        pass

    if opts.include_path is None:
        default_path = os.path.abspath(r".")
        sys.path.insert (0, default_path)
        print ("@@@ add default sys path:", default_path)     
    else:
        sys.path.insert (0, opts.include_path)
        print ("@@@ add sys path:", opts.include_path)
        
    DynTrace (opts.filename, opts.source)
    print ("Run successful.....")

if __name__ == "__main__":
   main()
