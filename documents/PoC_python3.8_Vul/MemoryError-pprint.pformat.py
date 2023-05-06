
from pprint import *
import pprint
import re
from io import StringIO

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, object, indent, width, depth):
        try:
            ret = pprint.pformat(object, indent, width, depth)
        except (AssertionError, AttributeError, LookupError, OSError, StopIteration, TypeError, ValueError) as e:
            pass

object = {"{3743535432: '/tmp/fuzzing-test', 4015984643K\x00: 'www.python.org', 212282ignore_crashes1883: '/tmp/fuzzin\x17\x00test', 2978728783: '/tmp/3743535432: '/tmp/fuzzing-test', 4015984643K\x00: 'www.python.org', 212282ignore_crashes1883: '/tmp/fuzzin\x17\x00test', 2978728783: '/tmp/fuzzing-tes20440960:(450459311, 2327341393: 'www.python.org', 4074200ne}: '/tmp/fu=zin\x17"}
indent = 287231826372318263
width  = 24
depth  = 24

           
dc = demoCls()
dc.demoFunc(object, indent, width, depth)
