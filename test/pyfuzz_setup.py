
import os
import sys
import importlib
import random
from fuzzwrap import *

SrvPort = random.randint(10000, 65531) 

if True == SetupPyFuzz('../experiments/apispec.xml', SrvPort):
    print ("SetupPyFuzz setup success")
else:
    print ("SetupPyFuzz setup Fail")

Done ()
sys.exit (0)




    
