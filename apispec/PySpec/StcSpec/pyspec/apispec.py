
# _*_ coding:utf-8 _*_
import os

ExcepList = ['__pycache__', 'test', 'site-packages', 'importlib', 'concurrent', 'subprocess', 'multiprocessing', 'traceback',
             'distutils', 'lib2to3', 'turtledemo', 'asyncio', 'pdb', 'pkgutil', 'turtle', 'inspect', 'trace', 'tkinter']

class PyApi ():
    def __init__ (self, ApiName, Expr, Ret, Args, PosArgs, KwoArgs, Defas, KwoDefas, Deps):
        self.ApiName = ApiName
        self.Expr    = Expr
        self.Ret     = Ret
        self.Args    = Args
        self.PosArgs = PosArgs
        self.KwoArgs = KwoArgs

        self.Defas = Defas
        self.KwoDefas = KwoDefas

        self.Deps = Deps
        
class PyCls ():
    def __init__ (self, clsName, Init):
        self.clsName = clsName
        self.clsInit = Init
        self.Apis = {}

class PyExcep ():
    def __init__ (self, exName):
        self.exName  = exName

class PyMod ():
    def __init__ (self, mdName):
        self.Name    = mdName
        self.Apis    = {}
        self.Classes = {}       
        self.Exceptions = []

class PyLib ():
    def __init__ (self, Name):
        self.Name  = Name
        self.Modules = {}
        self.Exceptions = []
