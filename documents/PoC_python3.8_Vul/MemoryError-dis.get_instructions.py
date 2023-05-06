
from dis import *
import dis
import argparse
import io


class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, x):
        try:
            ret = dis.get_instructions(x)
        except (AssertionError, AttributeError, LookupError, OSError, SyntaxError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError) as e:
            pass

dc = demoCls()
dc.demoFunc("rf((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((rom%r=f")
