import os
import sys
import importlib
import traceback
import atheris

PYFUZZ_SCRIPT = 'PYFUZZ_SCRIPT'
PYFUZZ_SCRIPT_API_TYPE = 'PYFUZZ_SCRIPT_API_TYPE'


def PyLv2Mutate (Data, MaxSize, Seed):
    #print ("[%s] PYFUZZ_SCRIPT_API_TYPE = %s, MaxSize = %d" %(os.environ[PYFUZZ_SCRIPT], os.environ[PYFUZZ_SCRIPT_API_TYPE], MaxSize))
    if MaxSize != 0:
        try:
            Indicator = int (Data [0:1])
            if Indicator%2 == 0:
                return atheris.Mutate(Data, MaxSize)
            else:
                TypeList = eval (os.environ[PYFUZZ_SCRIPT_API_TYPE])
                Ret =  atheris.PyEncode (TypeList)
                print ("[PyLv2Mutate] entry atheris.PyEncode...................." + str(Ret))
                return Ret
        except:
            return atheris.Mutate(Data, MaxSize)
    else:
        return atheris.Mutate(Data, MaxSize)
        

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

    try:
        SeedList = os.listdir(pyScriptCorpus)
        if len (SeedList) == 0:
            os.removedirs (pyScriptCorpus)
    except Exception as e:
        print (e)


def RunScript (script, Input='0000000000', Print=False):

    absPath  = os.path.abspath (script)
    absDir   = os.path.dirname (absPath)
    baseName = os.path.basename (script)

    if absDir not in sys.path:
        sys.path.insert(0, absDir)

    md  = baseName.split('.')[0]
    lib = importlib.import_module(md)
    
    try:
        lib.RunFuzzer (Input)
    except Exception as e:
        if Print == True:
            traceback.print_exc()
        return e.__class__.__name__
    
    return 'True'

