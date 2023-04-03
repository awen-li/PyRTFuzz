
import os
import sys
import random
from fuzzwrap import *
from platform import python_version

py_version = python_version()

SrvPort = random.randint(10000, 65531) 

if True == SetupPyFuzz('../apispec/PySpec/apispec.xml', SrvPort, ProbAll=False):
    print ("SetupPyFuzz setup success")
else:
    SendEndReq ()
    sys.exit (0)

SeedDir = f'../experiments/seeds_python{py_version}'
InitFlag = SeedDir + '/initial_done'
if os.path.exists (InitFlag):
    os.system (f"rm -rf {SeedDir}/*")

Ret = GetInitialSeeds (SeedDir)
if Ret == 'done':
    if not os.path.exists (InitFlag):
        print ("### Warning: Initialization Flag Missing!")
    print ("GetInitialSeeds success with Action: initial")
else:
    print ("GetInitialSeeds fail with Action[%s]: initial" %Ret)
    
Done ()
sys.exit (0)





    
