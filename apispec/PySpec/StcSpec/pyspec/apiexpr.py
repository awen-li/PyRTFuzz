import os
import numpy as np
from .apispec_load import *

class ApiExpr ():
    def __init__ (self, ApiSpec='apispec.xml'):
        self.PyLibs = self.InitPyLibs (ApiSpec)

    def GenExpr (self):
        for libName, pyLib in self.PyLibs.items ():
            for mdName, pyMoudle in pyLib.Modules.items ():
                for clsName, cls in pyMoudle.Classes.items ():
                    for apiName, api in cls.Apis.items ():
                        pass

                for apiName, api in pyMoudle.Apis.items ():
                    pass