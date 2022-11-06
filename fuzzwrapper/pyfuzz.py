#!/usr/bin/python
import os
import sys
import importlib
import atheris

atheris.InstrumentLibs()


def TestDriver(script, data):
    md = os.basename (script)
    lib = importlib.import_module(py)
    lib.RunFuzz (data)
    
if __name__ == '__main__':
    atheris.Setup(sys.argv, TestDriver, enable_python_coverage=True)
    while True:
        atheris.FuzzPyCore(300)
        atheris.FuzzNext ()

    
