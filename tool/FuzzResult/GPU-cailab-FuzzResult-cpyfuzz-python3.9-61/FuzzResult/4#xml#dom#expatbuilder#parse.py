from fuzzwrap import PyDecode 
from xml.dom.expatbuilder import *
import xml
import xml.dom
import xml.dom.expatbuilder
from xml.dom import EMPTY_NAMESPACE
from xml.dom import EMPTY_PREFIX
from xml.dom import Node
from xml.dom import XMLNS_NAMESPACE
from xml.dom import minidom
from xml.dom import xmlbuilder
from xml.parsers import expat

API_TYPE_LIST = ['str', 'bool']

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            (file, namespaces) = PyDecode(API_TYPE_LIST, arg)
            ret = xml.dom.expatbuilder.parse(file, namespaces)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, xml.dom.expatbuilder.ParseEscape) as e:
            pass

def RunFuzzer(x):
    PyCall_1681878279_zauhg(x)

def PyCall_1681878279_zauhg(x):
    dc = demoCls()
    dc.demoFunc(x)
