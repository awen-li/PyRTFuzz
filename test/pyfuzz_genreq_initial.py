
import os
import sys
import random
import atheris

SrvPort = random.randint(10000, 65531) 

if True == atheris.SetupPyFuzz('../apispec/PySpec/apispec.xml', SrvPort, ProbAll=False):
    print ("atheris.SetupPyFuzz setup success")
else:
    atheris.SendEndReq ()
    sys.exit (0)

InitFlag = '../experiments/seeds/initial_done'
if os.path.exists (InitFlag):
    os.remove (InitFlag)

Ret = atheris.GetInitialSeeds ('../experiments/seeds')
if Ret == 'done':
    if not os.path.exists (InitFlag):
        print ("### Warning: Initialization Flag Missing!")
    print ("atheris.GetInitialSeeds success with Action: initial")
else:
    print ("atheris.GetInitialSeeds fail with Action[%s]: initial" %Ret)
    
atheris.Done ()
sys.exit (0)





    
