import os
import sys, getopt
import argparse
import time
from pygen import *


InitTicks = time.time()

def TIME_COST (Name):
    print ("@@@@ ", Name, " time cost: ", str (time.time() - InitTicks))


def InitArgument (parser):
    parser.add_argument('--version', action='version', version='trace 2.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')
    grp.add_argument('-g', '--generate', action='store_true', help='generate python app')
    grp.add_argument('-d', '--debug', nargs='?', help='debug switch: 0-close, 1-open')
                     
    parser.add_argument('filename', nargs='?', help='source dir to process')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')


def main():
    parser = argparse.ArgumentParser()
    InitArgument (parser)
    opts = parser.parse_args()

    if opts.debug:
        print ('opts.debug is ' + opts.debug)
        SetDebug (opts.debug)

    if opts.generate:
        if opts.filename is None:
            parser.error('filename is missing: required with the main options')

        ag = AppGen (opts.filename)
        ag.Gen ()

        core = Core (opts.filename)
        core.GenApp ('')
    else:
        pass

    print ("Run successful.....")

if __name__ == "__main__":
   main()
