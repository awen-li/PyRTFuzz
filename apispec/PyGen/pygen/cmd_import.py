import random
import string
import astunparse
import ast
from ast import *
from .astop import *
from .debug import *

class PyImport(AstOp):
    Tmpt = "from x import *"
    def __init__(self):
        super(PyImport, self).__init__(PyImport.Tmpt)
        pass