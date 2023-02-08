
import os
import sys
import atheris

if True == atheris.SetupPyFuzz('/home/wen/CpyFuzz/apispec/PySpec/apispec.xml', 19163):
    print ("atheris.SetupPyFuzz setup success")
else:
    atheris.SendEndReq ()
    sys.exit (0)

Ret = atheris.SendWeightedReq ('update', '/home/wen')
if Ret == 'done':
	print ("atheris.SendWeightedReq success")
else:
    print ("atheris.SendWeightedReq fail")
    
atheris.SendEndReq ()
sys.exit (0)





    
