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
                     
    parser.add_argument('filename', nargs='?', help='source dir to process')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')


def main():
    parser = argparse.ArgumentParser()
    InitArgument (parser)
    opts = parser.parse_args()

    if opts.generate:
        if opts.filename is None:
            parser.error('filename is missing: required with the main options')

        apiSpec = ApiSpec (opts.filename)
        apiSpec.Parser ()

        ag = AppGen ()
        ag.Gen ()
    else:
        pass

    print ("Run successful.....")

if __name__ == "__main__":
   main()
