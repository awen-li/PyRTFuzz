#!/usr/bin/python

import os
import sys, getopt
import argparse
import time
from astwalk import ParsePyFile


def InitArgument (parser):
    parser.add_argument('--version', action='version', version='trace 2.0')
    
    grp = parser.add_argument_group('Main options', 'One of these (or --report) must be given')                    
    parser.add_argument('dirname', nargs='?', help='source dir to process')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='arguments to the program')


def main():
    parser = argparse.ArgumentParser()
    InitArgument (parser)

    opts = parser.parse_args()
    if opts.dirname is None:
        parser.error('dirname is missing: required with the main options')

    ParsePyFile (opts.dirname)

    print ("Run successful.....")

if __name__ == "__main__":
   main()
