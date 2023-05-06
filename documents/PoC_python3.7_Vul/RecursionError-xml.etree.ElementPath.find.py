
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
            ret = xml.etree.ElementPath.find(elem, path)
        except (AssertionError, AttributeError, KeyError, LookupError, OSError, StopIteration, SyntaxError, TypeError, ValueError) as e:
            print (e)

with open ("xml.etree.ElementPath.find-elem", "rb") as F:
    elem = F.read ()
                

with open ("xml.etree.ElementPath.find-path", "r") as F1:
    path = F1.read ()

dc = demoCls()
dc.demoFunc(elem, path)
