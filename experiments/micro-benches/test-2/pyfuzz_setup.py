
import os
import sys
import importlib
import random
import atheris

SrvPort = random.randint(10000, 65531) 

if True == atheris.SetupPyFuzz('../../../apispec/PySpec/apispec.xml', SrvPort):
    print ("atheris.SetupPyFuzz setup success")
else:
    print ("atheris.SetupPyFuzz setup Fail")

atheris.SendEndReq ()
sys.exit (0)




    
