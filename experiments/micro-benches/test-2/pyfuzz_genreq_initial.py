
import os
import sys
import random
import atheris

SrvPort = random.randint(10000, 65531) 

if True == atheris.SetupPyFuzz('../../../apispec/PySpec/apispec.xml', SrvPort):
    print ("atheris.SetupPyFuzz setup success")
else:
    atheris.SendEndReq ()
    sys.exit (0)

Ret = atheris.GetInitialSeeds ('../../../experiments/seeds')
if Ret == 'done':
	print ("atheris.GetInitialSeeds success with Action: initial")
else:
    print ("atheris.GetInitialSeeds fail with Action: initial")
    
atheris.Done ()
sys.exit (0)





    
