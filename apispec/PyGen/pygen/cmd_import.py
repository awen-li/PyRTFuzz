
import astunparse
import ast

class PyImport():
    def __init__(self, PyModule):
        self.PyModule = PyModule

    def IsRef (self, App, Name):
        if App.find (Name) == -1:
            return False
        else:
            return True

    def GenImport (self, App):
        PMd = self.PyModule.Name.split ('.')[0]

        # self module
        Imports = "from fuzzwrap import PyDecode \n" +\
                  "import " + PMd + "\n"\
                  "from " + self.PyModule.Name + " import *"

        # Imports
        for Impt in self.PyModule.Imports:
            if Impt[0:1] == '_':
                continue

            if Impt.find (':') == -1:
                Name = Impt
                if self.IsRef (App, Name) == False:
                    continue
                Imports += '\n' + "import " + Name
            else:
                Name, AsName = Impt.split (':')
                if self.IsRef (App, Name) == False and self.IsRef (App, AsName) == False:
                    continue
                Imports += '\n' + "import " + Name + ' as ' + AsName

        # Importfrom
        for ImptFrom in self.PyModule.ImportFrom:
            md, al = ImptFrom.split (':')
            if md[0:1] == '_':
                continue
            if self.IsRef (App, md) == False and self.IsRef (App, al) == False:
                continue
            Imports += '\n' + "from " + md + ' import ' + al

        Imports += '\n'
        return Imports