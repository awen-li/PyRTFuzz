
import astunparse
import ast

class PyImport():
    def __init__(self, PyModule):
        self.PyModule = PyModule

    def GenImport (self, App):
        PMd = self.PyModule.Name.split ('.')[0]

        # self module
        Imports = "from atheris import PyfDecode \n" +\
                  "import " + PMd + "\n"\
                  "from " + self.PyModule.Name + " import *"

        # Imports
        for Impt in self.PyModule.Imports:
            if Impt[0:1] == '_':
                continue
            if App.find (Impt) == -1:
                continue
            Imports += '\n' + "import " + Impt

        # Importfrom
        for ImptFrom in self.PyModule.ImportFrom:
            md, al = ImptFrom.split (':')
            if md[0:1] == '_':
                continue
            if App.find (md) == -1 and App.find (al) == -1:
                continue
            Imports += '\n' + "from " + md + ' import ' + al

        Imports += '\n'
        return Imports