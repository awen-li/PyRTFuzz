
import os
import sys
import atheris

if True == atheris.SetupPyFuzz('/home/wen/CpyFuzz/apispec/PySpec/apispec.xml', 19163):
    print ("atheris.SetupPyFuzz setup success")
else:
    atheris.SendEndReq ()
    sys.exit (0)

Ret = atheris.SendGenReq ('initial', '/home/wen')
if Ret == 'done':
	print ("atheris.SendGenReq success with Action: initial")
else:
    print ("atheris.SendGenReq fail with Action: initial")
    
Ret = atheris.SendGenReq ('random', '/home/wen')
if os.path.exists (Ret):
	print ("atheris.SendGenReq success with Action: random -> " + Ret)
else:
    print ("atheris.SendGenReq fail with Action: random")
    
Ret = atheris.SendGenReq ('weighted', '/home/wen')
if os.path.exists (Ret):
	print ("atheris.SendGenReq success with Action: weighted -> " + Ret)
else:
    print ("atheris.SendGenReq fail with Action: weighted")
    
atheris.SendEndReq ()
sys.exit (0)





    
