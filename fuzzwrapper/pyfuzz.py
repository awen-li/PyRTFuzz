
import os
import sys
import importlib
import random
import atheris

SrvPort = random.randint(10000, 65531)
try:
    atheris.SetupPyFuzz('apispec.xml', SrvPort)
    atheris.GetInitialSeeds ('seeds')
except:
    sys.exit (0)

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
    atheris.SetLv2Driver (lib.RunFuzzer, pyScriptCorpus)
    atheris.FuzzLv2()

    
if __name__ == '__main__':
    atheris.SetupCore(sys.argv,
                      PyCoreFuzz,
                      atheris.GetRandomSeed,
                      atheris.GetSpecifiedSeed,
                      enable_python_coverage=True)
    atheris.FuzzLv1(300)
    atheris.Done ()
 
