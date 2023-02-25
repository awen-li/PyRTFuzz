
import os
from progressbar import ProgressBar
from .apispec_gen import *
from .apispec_load import *

class ApiSpecMerge ():
    SupportMerge = ['exc']

    def __init__ (self, ToSpec, FromSpec, MergeField):
        self.ToSpec   = self.GetApiSpec (ToSpec)
        self.FromSpec = self.GetApiSpec (FromSpec)
        self.MergeField = MergeField

    def GetApiSpec (self, SpecPath):
        apiSpec = ApiSpecLoader (SpecPath)
        apiSpec.Parser ()
        return apiSpec.PyLibs
    
    def SavePyLibs (self, path='merge-apispec.xml'):
        pyLibs = []
        for _, lib in self.ToSpec.items ():
            pyLibs.append (lib)
        
        ApiSpecGen.WriteXml (pyLibs, path)
    
    def GetModule (self, Spec, Lib, Module):
        for libName, pyLib in Spec.items ():
            if libName != Lib:
                continue
            for mdName, pyMoudle in pyLib.Modules.items ():
                if mdName != Module:
                    continue
                return pyMoudle
        return None
    
    def MergeExc (self):
        par = ProgressBar ()
        for libName, pyLib in par(self.ToSpec.items ()):
            for mdName, pyMoudle in pyLib.Modules.items ():
                FMD = self.GetModule (self.FromSpec, libName, mdName)
                pyMoudle.Exceptions += FMD.Exceptions
    
    def Merge (self):
        if self.MergeField == 'exc':
            self.MergeExc ()
        else:
            print ("Suport merge: " + str (ApiSpecMerge.SupportMerge))

        self.SavePyLibs ()
