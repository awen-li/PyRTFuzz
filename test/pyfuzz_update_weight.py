
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

Ret = atheris.UpdateWeight ('../../../')
if Ret == 'done':
	print ("atheris.SendWeightedReq success")
else:
    print ("atheris.SendWeightedReq fail")
    
atheris.Done ()
sys.exit (0)





    
