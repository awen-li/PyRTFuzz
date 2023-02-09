
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

Ret = atheris.SendGenReq ('initial', '/home/wen/CpyFuzz/experiments/seeds')
if Ret == 'done':
	print ("atheris.SendGenReq success with Action: initial")
else:
    print ("atheris.SendGenReq fail with Action: initial")
    
atheris.SendEndReq ()
sys.exit (0)





    
