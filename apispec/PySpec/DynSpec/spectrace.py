
import os
import sys, getopt
import argparse
from pytrace import *

TracingDone='/tmp/TracingDone'

def InitArgument (parser):
    parser.add_argument('--version', action='version', version='trace 2.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')
    grp.add_argument('-s', '--source',
                     help='source api spec xml')
    grp.add_argument('-p', '--prefix',
                     help='the prefix of current tracing file')
    grp.add_argument('-i', '--include_path',
                     help='the installation path of the target')
              
    parser.add_argument('filename', nargs='?', help='file to run as main program')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')

def DynTrace (Entry, ApiSpecXml, Prefix):
    fIndex = Entry.rfind ('/')
    if fIndex != -1:
        Path = Entry [0:fIndex]
        Entry = Entry [fIndex+1:]
        os.chdir (Path)

    try:
        print ("### Trace start -> " + os.getcwd () + ": " + Entry)   
        with open(Entry) as fp:
            code = compile(fp.read(), Entry, 'exec')

        globs = {
            '__file__': Entry,
            '__name__': '__main__',
            '__package__': None,
            '__cached__': None,
        }

        if os.path.exists (TracingDone):
            os.remove (TracingDone)

        sys.argv = [Entry]
        with Tracing (ApiSpecXml, PyLibPath=Prefix) as T:
            exec(code, globs, globs)

    except OSError as oserr:
        sys.exit("Cannot run file %s because: %s" % (Entry, oserr))
    except SystemExit as sysrr:
        with open (TracingDone, 'w') as F:
            print (TracingDone, file=F)


def main():
    parser = argparse.ArgumentParser()
    InitArgument (parser)

    opts = parser.parse_args() 
    sys.argv = [opts.filename, *opts.arguments]

    if opts.filename is None:
        parser.error('filename or dirname is missing: required with the main options')
        
    if opts.source is None:
        opts.source = 'apispec.xml'
        if not os.path.exists (opts.source):
            parser.error('please specify the original api spec xml')
        opts.source = os.path.abspath (opts.source)

    if opts.include_path is None:
        default_path = os.path.abspath(r".")
        sys.path.insert (0, default_path)
        print ("### add default sys path:", default_path)     
    else:
        sys.path.insert (0, opts.include_path)
        print ("### add sys path:", opts.include_path)

    if os.path.isfile (opts.filename):
        DynTrace (opts.filename, opts.source, opts.prefix)
    elif os.path.isdir(opts.filename):
        IterTc = IterTracing (opts.source)
        IterTc.StartTracing (opts.filename)
    else:
        print ("\n### could not find %s, please make sure run the tool in correct directory!\n" %opts.filename)
        return
    
    print ("Run successful.....")

if __name__ == "__main__":
   main()
