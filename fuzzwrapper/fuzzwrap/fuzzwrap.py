import os
import sys
import importlib
import traceback
import time
import atheris
from .data_encode import PyEncode

PYFUZZ_SCRIPT = 'PYFUZZ_SCRIPT'
PYFUZZ_SCRIPT_API_TYPE = 'PYFUZZ_SCRIPT_API_TYPE'
SEED_ITERATION_BUDGET = 1024

SeedIterNum = SEED_ITERATION_BUDGET

def PyLv2Mutate (Data, MaxSize, Seed):
    global SeedIterNum
    #print ("[%s] PYFUZZ_SCRIPT_API_TYPE = %s, MaxSize = %d" %(os.environ[PYFUZZ_SCRIPT], os.environ[PYFUZZ_SCRIPT_API_TYPE], MaxSize))
    if MaxSize != 0:
        try:
            LasUpdate = atheris.GetCovUpdateDuration ()
            Duration = LasUpdate>>16
            TimeBudget = LasUpdate&0xFFFF    
            #print ("### [PyLv2Mutate][%d]Duration = %d, TimeBudget = %d" %(LasUpdate, Duration, TimeBudget))
            
            if Duration <= TimeBudget/4 or SeedIterNum > 0:
                SeedIterNum -= 1
                return atheris.Mutate(Data, MaxSize)
            else:
                SeedIterNum = SEED_ITERATION_BUDGET
                TypeList = eval (os.environ[PYFUZZ_SCRIPT_API_TYPE])
                Ret =  PyEncode (TypeList)
                #print ("\n### [PyLv2Mutate] Duration=%d/%d, PyEncode: %s" %(Duration, TimeBudget, str(Ret)))
                return Ret
        except Exception as e:
            print (e)
            return atheris.Mutate(Data, MaxSize)
    else:
        return atheris.Mutate(Data, MaxSize)
        
def _Lv2InitialCorpus (TypeList, pyScriptCorpus, InitialNum=10):
    if not os.path.exists (pyScriptCorpus):
        os.mkdir (pyScriptCorpus, mode=711)
    while InitialNum > 0:
        InitialSeed = pyScriptCorpus + f'/{InitialNum}-initial.seed'
        with open (InitialSeed, 'w') as F:
            Ret =  PyEncode (TypeList)
            F.write (Ret.decode())
        InitialNum -= 1

def PyCoreFuzz (script):
    global SeedIterNum
    SeedIterNum = SEED_ITERATION_BUDGET

    absPath  = os.path.abspath (script)
    absDir   = os.path.dirname (absPath)
    baseName = os.path.basename (script)

    if absDir not in sys.path:
        sys.path.insert(0, absDir)
    
    # logging:
    with open ("CURRENT-level-fuzzing.log", 'w') as F:
        print (absPath, file=F)

    SctModule  = baseName.split('.')[0]
    FuzzMd = importlib.import_module(SctModule)
    
    # create corpus dir for the current script
    pyScriptCorpus = absDir + '/corpus'
    _Lv2InitialCorpus (FuzzMd.API_TYPE_LIST, pyScriptCorpus)

    # add env
    os.environ[PYFUZZ_SCRIPT] = script
    os.environ[PYFUZZ_SCRIPT_API_TYPE] = str(FuzzMd.API_TYPE_LIST)

    # set Lv2Driver
    atheris.SetLv2Driver (FuzzMd.RunFuzzer, pyScriptCorpus)

    IsExcepPass = os.getenv ("BYPASS_EXCEPTION")
    if IsExcepPass != None:
        print ("#########  Entry mask-exception fuzzing mode!")
        try:
            atheris.FuzzLv2()
        except:
            # Ignore all errors
            pass
    else:
        try:
            atheris.FuzzLv2()
        except (ValueError, TypeError, AttributeError, OSError, LookupError, 
                AssertionError, EOFError, ModuleNotFoundError, TypeError) as e:
            pass

    try:
        SeedList = os.listdir(pyScriptCorpus)
        if len (SeedList) == 0:
            os.removedirs (pyScriptCorpus)
    except Exception as e:
        print (e)
        sys.exit (0)

def RunScript (script, Input=None, Print=False, Silent=False):

    StartSec = time.time ()
    absPath  = os.path.abspath (script)
    absDir   = os.path.dirname (absPath)
    baseName = os.path.basename (script)

    if absDir not in sys.path:
        sys.path.insert(0, absDir)

    md  = baseName.split('.')[0]
    lib = importlib.import_module(md)

    stdout_bk = sys.stdout
    stderr_bk = sys.stderr
    
    Ret = 'True'
    try:
        if Input == None:
            Input = PyEncode (lib.API_TYPE_LIST).decode()
        
        if Silent == False:
            print ("### Running %s with inputs: %s" %(script, str(Input)))
        else:
            sys.stdout = open ('/dev/null', 'w')
            sys.stderr = open ('/dev/null', 'w')

        lib.RunFuzzer (Input)

        sys.stdout = stdout_bk
        sys.stderr = stderr_bk

    except Exception as e:
        sys.stdout = stdout_bk
        sys.stderr = stderr_bk
        
        if Print == True:
            traceback.print_exc()
        
        Ret = e.__class__.__name__
    finally:    
        print ("### Time Cost: %d (s)" %(time.time() - StartSec))
        return Ret
    
    


