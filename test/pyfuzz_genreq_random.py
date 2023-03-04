
import os
import sys
import random
from fuzzwrap import *

SrvPort = random.randint(10000, 65531) 

if True == SetupPyFuzz('../apispec/PySpec/apispec.xml', SrvPort, ProbAll=False):
    print ("SetupPyFuzz setup success")
else:
    SendEndReq ()
    sys.exit (0)
  
Ret = GetRandomSeed ('../experiments/seeds')
if os.path.exists (Ret):
	print ("GetRandomSeed success with Action: random -> " + Ret)
else:
    print ("GetRandomSeed fail with Action: random")
    
Done ()
sys.exit (0)





    
