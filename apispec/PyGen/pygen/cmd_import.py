
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
                  "from " + self.PyModule.Name + " import *\n" +\
                  "import " + PMd

        # Imports
        for Impt in self.PyModule.Imports:
            if Impt[0:1] == '_':
                continue

            if Impt.find (':') == -1:
                Name = Impt
                if self.IsRef (App, Name) == False or Name == PMd:
                    continue
                Imports += '\n' + "import " + Name
            else:
                Name, AsName = Impt.split (':')
                mdRef = self.IsRef (App, Name)
                alRef = self.IsRef (App, AsName)
                if mdRef == False and alRef == False:
                    continue

                if mdRef == True and Name != PMd:
                    Imports += '\n' + "import " + Name
                if alRef == True:
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