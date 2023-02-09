
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
    
Ret = atheris.SendGenReq ('specify', '/home/wen/CpyFuzz/experiments/seeds/1#xml#dom#minidom#Node#isSameNode.py')
if os.path.exists (Ret):
	print ("atheris.SendGenReq success with Action: specify -> " + Ret)
else:
    print ("atheris.SendGenReq fail with Action: specify")
    
atheris.SendEndReq ()
sys.exit (0)





    
