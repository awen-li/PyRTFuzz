
import os
from .astop import *
from .apispec import *


pg_tempt_oo = \
"""
class demoCls:
    def __init__(self):
        pass

    def demoFunc0(self):
        pass

    def demoFunc1(self, PYF_ARG1):
        pass

def RunFuzzer (x):
    pass
"""

pg_tempt_pro = \
"""
def demoFunc0 ():
    pass

def demoFunc1 (PYF_ARG1):
    pass

def RunFuzzer (x):
    pass
"""

pg_for = \
"""
for PYF_I in range (0, PYF_E):
    pass
"""

pg_inherit = \
"""
import io
import pickle

class Pickler(pickle.Pickler):
  def persistent_id(self, obj):
    return super().persistent_id(obj)

Pickler(io.BytesIO()).dump(42)
"""

#####################################################################################################
#####################################################################################################

class AppGen ():
    def __init__ (self, apiSpecXml):
        apiSpec = ApiSpec (apiSpecXml)
        apiSpec.Parser ()

        self.PyLibs = apiSpec.PyLibs

    def Gen (self):
        for libName, pyLib in self.PyLibs.items ():
            print ("# " + libName)
            curExcepts = pyLib.Exceptions
            for mdName, pyMoudle in pyLib.Modules.items ():
                print ("## " + mdName)
                for clsName, cls in pyMoudle.Classes.items ():
                    print ("### " + clsName + ": " + cls.clsInit)
                    for apiName, api in cls.Apis.items ():
                        print ("#### " + apiName + " ---> " + api.Expr)
                        OP = NewOO (cls.clsInit, api.Expr, curExcepts)
                        OP.GenApp ()

                for apiName, api in pyMoudle.Apis.items ():
                    print ("### " + apiName)
                
                
        

        


