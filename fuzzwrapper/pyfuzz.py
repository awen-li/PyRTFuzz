
import os
import sys
import importlib
import random
import atheris

PYFUZZ_SCRIPT = 'PYFUZZ_SCRIPT'
PYFUZZ_SCRIPT_API_TYPE = 'PYFUZZ_SCRIPT_API_TYPE'

SrvPort = random.randint(10000, 65531)
try:
    atheris.SetupPyFuzz('apispec.xml', SrvPort, ProbAll=False)
    atheris.GetInitialSeeds ('seeds')
except:
    sys.exit (0)

def PyLv2Mutate (Data, MaxSize, Seed):
    #print ("[%s] PYFUZZ_SCRIPT_API_TYPE = %s" %(os.environ[PYFUZZ_SCRIPT], os.environ[PYFUZZ_SCRIPT_API_TYPE]))
    Length = len (Data)
    if Length != 0:
        try:
            Indicator = int (Data [0:1])
            if Indicator%2 == 0:
                return atheris.Mutate(Data, len(Length))
            else:
                TypeList = eval (os.environ[PYFUZZ_SCRIPT_API_TYPE])
                return atheris.PyfEncode (TypeList)
        except:
            return atheris.Mutate(Data, len(Length))
    else:
        return atheris.Mutate(Data, len(Length))
        

def PyCoreFuzz (script):

    absPath  = os.path.abspath (script)
    absDir   = os.path.dirname (absPath)
    baseName = os.path.basename (script)

    if absDir not in sys.path:
        sys.path.insert(0, absDir)

    SctModule  = baseName.split('.')[0]
    FuzzMd = importlib.import_module(SctModule)
    
    # create corpus dir for the current script
    pyScriptCorpus = absDir + '/' + SctModule

    # add env
    os.environ[PYFUZZ_SCRIPT] = script
    os.environ[PYFUZZ_SCRIPT_API_TYPE] = str(FuzzMd.API_TYPE_LIST)

    # set Lv2Driver
    atheris.SetLv2Driver (FuzzMd.RunFuzzer, pyScriptCorpus)
    atheris.FuzzLv2()

    
if __name__ == '__main__':
    atheris.SetupCore(sys.argv,
                      PyCoreFuzz,
                      atheris.GetRandomSeed,
                      atheris.GetSpecifiedSeed,
                      enable_python_coverage=True,
                      custom_mutator=PyLv2Mutate)
    atheris.FuzzLv1(300)
    atheris.Done ()
 
