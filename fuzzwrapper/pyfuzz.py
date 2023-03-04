

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
    
if __name__ == '__main__':
    SrvPort = random.randint(10000, 65531)
    try:
        atheris.SetupPyFuzz('apispec.xml', SrvPort, ProbAll=False)

        SeedPath = _GetSeedDir ()
        if SeedPath == None:
            Exception("Please specify the seed directory with /-pycript/ parameter")
        
        atheris.GetInitialSeeds (SeedPath)
        Calibrate (SeedPath)
    except:
        sys.exit (0)

    atheris.SetupCore(sys.argv,
                      PyCoreFuzz,
                      atheris.GetRandomSeed,
                      atheris.GetSpecifiedSeed,
                      enable_python_coverage=True,
                      custom_mutator=PyLv2Mutate)
    atheris.FuzzLv1(300)
    atheris.Done ()
 
