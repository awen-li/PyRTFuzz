
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
            Imports += '\n' + "import " + Impt

        # Importfrom
        for ImptFrom in self.PyModule.ImportFrom:
            md, al = ImptFrom.split (':')
            Imports += '\n' + "from " + md + ' import ' + al

        Imports += '\n'
        return Imports