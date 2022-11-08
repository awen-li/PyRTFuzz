#!/usr/bin/python

import os


def main(data):
    curPath = os.getcwd ()
    Name = curPath + " ---> " + __file__
    print (Name)

def RunFuzz (data):
    main(data)
    
