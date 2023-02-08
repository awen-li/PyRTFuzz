
import os
import sys
import importlib
import atheris

if True == atheris.SetupPyFuzz('/home/wen/CpyFuzz/apispec/PySpec/apispec.xml', 19163):
    print ("atheris.SetupPyFuzz setup success")
else:
    print ("atheris.SetupPyFuzz setup Fail")

atheris.SendEndReq ()
sys.exit (0)




    
