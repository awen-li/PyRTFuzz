import sys
import random
import atheris
import psutil
from .fuzzsetup import *
from .calibrate import *
from .fuzzwrap import *

def _GetSeedDir ():
    for arg in sys.argv:
        if arg.find ("-pyscript=") == -1:
            continue
        return arg[arg.find('=')+1:]
    return None

def _ArgProc ():
    Index = 0
    for arg in sys.argv:
        if arg.find ("-lv2time=") != -1:
            sys.argv[Index] = arg.replace ("-lv2time=", "-max_total_time=")
            break
        Index += 1
    
    # default time budget
    if Index == len (sys.argv):
       sys.argv.append ("-max_total_time=90")

    # default memory budget
    sys.argv.append ("-rss_limit_mb=8192")


def FuzzEntry (CpuId):
    if CpuId != None:
        CurP = psutil.Process ()
        CurP.cpu_affinity([int(CpuId)])
        CurP.nice(0)
        print ("### Bind current process to CPU: %s with nice: %d\n" %(str(CurP.cpu_affinity()), CurP.nice()))

    SrvPort = random.randint(10000, 65531)
    try:
        SetupPyFuzz('apispec.xml', SrvPort, ProbAll=True)

        SeedPath = _GetSeedDir ()
        if SeedPath == None:
            raise Exception("Please specify the seed directory with /-pycript/ parameter")

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
    try:
        atheris.FuzzLv1()
        Done ()
        sys.exit (0)
    except:
        Done ()
        sys.exit (0)
