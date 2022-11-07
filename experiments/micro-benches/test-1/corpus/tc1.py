#!/usr/bin/python

import os


def main():
    curPath = os.getcwd ()
    Name = curPath + " ---> " + __file__
    print (Name)

def FuzzTest ():
    main()
    
