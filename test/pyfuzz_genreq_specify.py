
import os
import sys
import random
from fuzzwrap import *
from platform import python_version

py_version = python_version()

SrvPort = random.randint(10000, 65531) 

if True == SetupPyFuzz('../experiments/apispec.xml', SrvPort, ProbAll=False):
    print ("SetupPyFuzz setup success")
else:
    SendEndReq ()
    sys.exit (0)
    
Ret = GetSpecifiedSeed (f'../experiments/seeds_python{py_version}/xml.dom.minidom.Node.isSameNode/1#xml#dom#minidom#Node#isSameNode.py')
if os.path.exists (Ret):
	print ("GetSpecifiedSeed success with Action: specify -> " + Ret)
else:
    print ("GetSpecifiedSeed fail with Action: specify")
    
Done ()
sys.exit (0)





    
