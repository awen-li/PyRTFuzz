
import os
import sys
import random
from fuzzwrap import *

SrvPort = random.randint(10000, 65531) 

if True == SetupPyFuzz('../apispec/PySpec/apispec.xml', SrvPort, ProbAll=False):
    print ("SetupPyFuzz setup success")
else:
    SendEndReq ()
    sys.exit (0)

Ret = UpdateWeight ('../../../')
if Ret == 'done':
	print ("SendWeightedReq success")
else:
    print ("SendWeightedReq fail")
    
Done ()
sys.exit (0)





    
