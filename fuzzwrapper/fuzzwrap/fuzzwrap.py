import os
import sys
import importlib
import traceback
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
    atheris.FuzzLv2()

    try:
        SeedList = os.listdir(pyScriptCorpus)
        if len (SeedList) == 0:
            os.removedirs (pyScriptCorpus)
    except Exception as e:
        print (e)
        sys.exit (0)

def RunScript (script, Input=None, Print=False, Silent=False):

    absPath  = os.path.abspath (script)
    absDir   = os.path.dirname (absPath)
    baseName = os.path.basename (script)

    if absDir not in sys.path:
        sys.path.insert(0, absDir)

    md  = baseName.split('.')[0]
    lib = importlib.import_module(md)
    
    try:
        if Input == None:
            Input = PyEncode (lib.API_TYPE_LIST).decode()
        
        if Silent == False:
            print ("### Running %s with inputs: %s" %(script, str(Input)))
        
        sys.stdout = open ('/dev/null', 'w')
        sys.stderr = open ('/dev/null', 'w')

        lib.RunFuzzer (Input)

        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
    except Exception as e:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        
        if Print == True:
            traceback.print_exc()
        return e.__class__.__name__
    
    return 'True'

