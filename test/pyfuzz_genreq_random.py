
import os
import sys
import random
from fuzzwrap import *
from platform import python_version

py_version = python_version()

SrvPort = random.randint(10000, 65531) 

if True == SetupPyFuzz('../experiments/apispec.xml', SrvPort, ProbAll=False):
    print ("SetupPyFuzz setup success")
else:
    SendEndReq ()
    sys.exit (0)
  
Ret = GetRandomSeed (f'../experiments/seeds_python{py_version}')
if os.path.exists (Ret):
	print ("GetRandomSeed success with Action: random -> " + Ret)
else:
    print ("GetRandomSeed fail with Action: random")
    
Done ()
sys.exit (0)





    
