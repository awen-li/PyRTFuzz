
import astunparse
import ast

class PyImport():
    def __init__(self, PyModule):
        self.PyModule = PyModule

    def GenImport (self):
        # self module
        Imports = "from " + self.PyModule.Name + " import *"

        # Imports
        for Impt in self.PyModule.Imports:
            if Impt[0:1] == '_':
                continue
            Imports += '\n' + "import " + Impt

        # Importfrom
        for ImptFrom in self.PyModule.ImportFrom:
            md, al = ImptFrom.split (':')
            if md[0:1] == '_':
                continue
            Imports += '\n' + "from " + md + ' import ' + al

        Imports += '\n'
        return Imports