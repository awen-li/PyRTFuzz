

import sys
import random
import atheris
from fuzzwrap import *

def _GetSeedDir ():
    for arg in sys.argv:
        if arg.find ("-pyscript=") == -1:
            continue
        return arg[arg.find('=')+1:]
    return None

def _ArgProc ():
    index = 0
    for arg in sys.argv:
        if arg.find ("-lv2time=") != -1:
            sys.argv[index] = arg.replace ("-lv2time=", "-max_total_time=")
            break
        index += 1

if __name__ == '__main__':
    SrvPort = random.randint(10000, 65531)
    try:
        SetupPyFuzz('apispec.xml', SrvPort, ProbAll=False)

        SeedPath = _GetSeedDir ()
        if SeedPath == None:
            Exception("Please specify the seed directory with /-pycript/ parameter")
        
        GetInitialSeeds (SeedPath)
        Calibrate (SeedPath)
    except Exception as e:
        print (e)
        sys.exit (0)

    _ArgProc ()
    atheris.SetupCore(sys.argv,
                      PyCoreFuzz,
                      GetRandomSeed,
                      GetSpecifiedSeed,
                      enable_python_coverage=True,
                      custom_mutator=PyLv2Mutate)
    atheris.FuzzLv1()
    atheris.Done ()
 
