
import os
import sys
import random
import atheris

SrvPort = random.randint(10000, 65531) 

if True == atheris.SetupPyFuzz('/home/wen/CpyFuzz/apispec/PySpec/apispec.xml', SrvPort):
    print ("atheris.SetupPyFuzz setup success")
else:
    atheris.SendEndReq ()
    sys.exit (0)
  
Ret = atheris.SendGenReq ('random', '/home/wen/CpyFuzz/experiments/seeds')
if os.path.exists (Ret):
	print ("atheris.SendGenReq success with Action: random -> " + Ret)
else:
    print ("atheris.SendGenReq fail with Action: random")
    
atheris.SendEndReq ()
sys.exit (0)





    
