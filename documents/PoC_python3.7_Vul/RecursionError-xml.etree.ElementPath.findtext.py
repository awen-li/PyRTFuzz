
from xml.etree.ElementPath import *
import xml
import re
import xml.etree
import xml.etree.ElementPath

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, elem, path):
        try:
            ret = xml.etree.ElementPath.findtext(elem, path, "")
        except (AssertionError, AttributeError, KeyError, LookupError, OSError, StopIteration, SyntaxError, TypeError, ValueError) as e:
            pass

with open ("xml.etree.ElementPath.findtext-elem", "rb") as F:
    elem = F.read ()
                
with open ("xml.etree.ElementPath.findtext-path", "r") as F:
    path = F.read ()
    
dc = demoCls()
dc.demoFunc(elem, path)
