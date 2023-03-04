
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

InitFlag = '../experiments/seeds/initial_done'
if os.path.exists (InitFlag):
    os.system ("rm -rf ../experiments/seeds/*")

Ret = GetInitialSeeds ('../experiments/seeds')
if Ret == 'done':
    if not os.path.exists (InitFlag):
        print ("### Warning: Initialization Flag Missing!")
    print ("GetInitialSeeds success with Action: initial")
else:
    print ("GetInitialSeeds fail with Action[%s]: initial" %Ret)
    
Done ()
sys.exit (0)





    
