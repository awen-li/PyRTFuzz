
import os
import sys
import importlib
import atheris

if True == atheris.SetupPyFuzz('/home/wen/CpyFuzz/apispec/PySpec/apispec.xml', 19163):
    print ("atheris.SetupPyFuzz setup success")
else:
    atheris.SendEndReq ()
    sys.exit (0)

Ret = atheris.SendGenReq ('initial', '/home/wen')
if Ret == 'done':
	print ("atheris.SendGenReq success")
else:
    print ("atheris.SendGenReq fail")
    
atheris.SendEndReq ()
sys.exit (0)





    
