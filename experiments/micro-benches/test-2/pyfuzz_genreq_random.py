
import os
import sys
import random
import atheris

SrvPort = random.randint(10000, 65531) 

if True == atheris.SetupPyFuzz('../../../apispec/PySpec/apispec.xml', SrvPort, ProbAll=False):
    print ("atheris.SetupPyFuzz setup success")
else:
    atheris.SendEndReq ()
    sys.exit (0)
  
Ret = atheris.GetRandomSeed ('../../../experiments/seeds')
if os.path.exists (Ret):
	print ("atheris.GetRandomSeed success with Action: random -> " + Ret)
else:
    print ("atheris.GetRandomSeed fail with Action: random")
    
atheris.Done ()
sys.exit (0)





    
