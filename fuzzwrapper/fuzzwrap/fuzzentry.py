import sys
import random
import atheris
import psutil
from .fuzzsetup import *
from .calibrate import *
from .fuzzwrap import *

def _Log (Log, Msg=None):
    if Log == None:
        return
    Log (Msg)

def _GetSeedDir ():
    for arg in sys.argv:
        if arg.find ("-pyscript=") == -1:
            continue
        return arg[arg.find('=')+1:]
    return None


def FuzzEntry (CpuId, ProbAll, Log=None):
    if CpuId != None:
        CurP = psutil.Process ()
        CurP.cpu_affinity([int(CpuId)])
        CurP.nice(0)
        print ("### Bind current process to CPU: %s with nice: %d\n" %(str(CurP.cpu_affinity()), CurP.nice()))

    SrvPort = random.randint(10000, 65531)
    try:
        SetupPyFuzz('apispec.xml', SrvPort, ProbAll=ProbAll)

        SeedPath = _GetSeedDir ()
        if SeedPath == None:
            raise Exception("Please specify the seed directory with /-pycript/ parameter")

        GetInitialSeeds (SeedPath)
        Calibrate (SeedPath)
    except Exception as e:
        print (e)
        sys.exit (0)

    # default memory budget
    sys.argv.append ("-rss_limit_mb=8192")

    atheris.SetupCore(sys.argv,
                      PyCoreFuzz,
                      GetRandomSeed,
                      GetSpecifiedSeed,
                      enable_python_coverage=True,
                      custom_mutator=PyLv2Mutate)
    try:
        atheris.FuzzLv1()
        _Log (Log, "### atheris.FuzzLv1() exit without exception")
    except Exception as e:
        _Log (Log, "### atheris.FuzzLv1() exit with exception: " + str(e))   
    finally:
        sys.exit (0)

def SysArg (Key):
    for arg in sys.argv:
        if arg.find (Key) != -1:
            return True
    return False

def DisableDisorder (Log=None):
    if SysArg ("disorder=0") == True:
        return
    sys.argv.append ("-disorder=0")
    _Log (Log, f"### DisableDisorder with -disorder=0")

def BindCpu (Log=None):
    newArgv = []
    Cpu = None
    for arg in sys.argv:
        if arg.find ('-cpu=') != -1:
            Cpu = arg[arg.find('=')+1:]
        else:
            newArgv.append (arg)
    
    if Cpu != None:
        sys.argv = newArgv
        _Log (Log, f"### bindding to CPU: {Cpu}")
    return Cpu

def Maskexcp (Log=None):
    newArgv = []
    Mask = False
    for arg in sys.argv:
        if arg.find ('-maskexcp') != -1:
            Mask = True
        else:
            newArgv.append (arg)

    if Mask == True:
        sys.argv = newArgv
        os.environ ['PYRTF_BYPASS_EXCEPTION'] = 'True'
        _Log (Log, "### set PYRTF_BYPASS_EXCEPTION True!")

        DisableDisorder (Log)
    return

def SLComplex (Log=None):
    newArgv = []
    Complex = None
    for arg in sys.argv:
        if arg.find ('-complex') != -1:
            Complex = arg[arg.find('=')+1:]
        else:
            newArgv.append (arg)

    if Complex != None:
        sys.argv = newArgv
        os.environ ['PYRTF_COMPLEXITY'] = Complex
        _Log (Log, f"### set Complex as {Complex}!")

        os.environ ['PYRTF_BYPASS_EXCEPTION'] = 'True'
        _Log (Log, "### set PYRTF_BYPASS_EXCEPTION True!")
        
        DisableDisorder ()
    return

def ProbPy (Log=None):
    newArgv = []
    ProbAll = True
    for arg in sys.argv:
        if arg.find ('-nopy') != -1:
            ProbAll = False
        else:
            newArgv.append (arg)

    if ProbAll == False:
        sys.argv = newArgv
        _Log (Log, f"### No instrument for Python code")
    return ProbAll

def DTyped (Log=None):
    newArgv = []
    Untyped = False
    Typed = False
    for arg in sys.argv:
        if arg.find ('-typed') != -1:
            Typed = True
        elif arg.find ('-untyped') != -1:
            Untyped = True
        else:
            newArgv.append (arg)

    if Untyped == True or Typed == True:
        # in typed/untyped mode, open maskexcp
        os.environ ['PYRTF_BYPASS_EXCEPTION'] = 'True'
        _Log (Log, "### set PYRTF_BYPASS_EXCEPTION True!")

        sys.argv = newArgv
        DisableDisorder ()
    
    if Untyped == True:
        os.environ ['PYRTF_UNTYPED'] = 'True'
        _Log (Log, "### set PYRTF_UNTYPED True!")

    return

def TimeBudget (Log=None):
    Budget = None
    newArgv = []
    for arg in sys.argv:
        if arg.find ("-lv2budget") != -1:
            Budget = arg[arg.find('=')+1:]
        else:
            newArgv.append (arg)
    
    # default time budget
    sys.argv = newArgv
    if Budget == None:
       sys.argv.append ("-max_total_time=90")
       _Log (Log, "### set LEVEL-2 budget as 90 (s)")
    else:
        sys.argv.append (f"-max_total_time={Budget}")
        _Log (Log, f"### set LEVEL-2 budget as {Budget} (s)")

def ArgHanlde (Log=None):
    Maskexcp (Log)
    DTyped (Log)
    SLComplex (Log)
    TimeBudget (Log)

    CpuId = BindCpu (Log)
    ProbAll = ProbPy (Log)

    return CpuId, ProbAll