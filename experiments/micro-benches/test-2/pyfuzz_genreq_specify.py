
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
    
Ret = atheris.GetSpecifiedSeed ('../../../experiments/seeds/1#xml#dom#minidom#Node#isSameNode.py')
if os.path.exists (Ret):
	print ("atheris.GetSpecifiedSeed success with Action: specify -> " + Ret)
else:
    print ("atheris.GetSpecifiedSeed fail with Action: specify")
    
atheris.Done ()
sys.exit (0)





    
