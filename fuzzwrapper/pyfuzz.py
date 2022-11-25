#!/usr/bin/python
import os
import sys
import importlib
import atheris

atheris.InstrumentLibs()


def PyCoreFuzz (script):

    absPath  = os.path.abspath (script)
    absDir   = os.path.dirname (absPath)
    baseName = os.path.basename (script)
    print ("@@@ PyCoreFuzz -> " + absDir + "  --->  " + baseName)

    if absDir not in sys.path:
        sys.path.insert(0, absDir)

    md  = baseName.split('.')[0]
    lib = importlib.import_module(md)
    
    # create corpus dir for the current script
    pyScriptCorpus = absDir + '/' + md

    # set Lv2Driver
    atheris.SetLv2Driver (lib.RunFuzz, pyScriptCorpus)
    atheris.FuzzLv2()

    
if __name__ == '__main__':
    atheris.SetupCore(sys.argv, PyCoreFuzz, enable_python_coverage=True)
    atheris.FuzzLv1(300)

    
