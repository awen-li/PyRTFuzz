from locale import *
import locale
import re
from builtins import str

def demoFunc(arg1,arg2,arg3,arg4):
    try:
        ret = locale.format(arg1,arg2,arg3,arg4)
    except (AssertionError, AttributeError, Error, ImportError, LookupError, NameError, OSError, TypeError, ValueError) as e:
        pass

percent = "%777777777777777u"
value = 2.0
grouping = True
monetary = True
demoFunc(percent, value, grouping, monetary)
