import os
import sys, getopt
import argparse
from pyspec import *


def InitArgument (parser):
    parser.add_argument('--version', action='version', version='specgen 1.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')
    grp.add_argument('-d', '--debug', action='store_true', help='generate python app')
                     
    parser.add_argument('dirname', nargs='?', help='source dir to process')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')


def main():
    parser = argparse.ArgumentParser()
    InitArgument (parser)
    opts = parser.parse_args()

    if opts.debug:
        SetDebug (1)

    apis = ApiSpec (opts.dirname)
    apis.GenSpec ()
    
    print ("Run successful.....")

if __name__ == "__main__":
   main()
