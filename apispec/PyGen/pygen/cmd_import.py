
import astunparse
import ast

class PyImport():
    def __init__(self, ApiPath):
        self.ApiPath = ApiPath

    def GenApp (self):
        Module = self.ApiPath.split ('.')[0]
        Impt = f"from {Module} import *"
        return Impt