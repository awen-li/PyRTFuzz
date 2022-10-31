#!/usr/bin/python

import os
import importlib

dyncall_list = ["tc1", "tc2", "tc3"]


def main():
    for py in dyncall_list:
        if True:
            lib = importlib.import_module(py)
            lib.FuzzTest ()
        

main()
    
