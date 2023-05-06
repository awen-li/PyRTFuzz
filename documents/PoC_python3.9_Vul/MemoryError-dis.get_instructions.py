from dis import *
import dis
import argparse
import io


class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg):
        try:
            ret = dis.get_instructions(arg)
        except (AssertionError, AttributeError, LookupError, OSError, SyntaxError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError) as e:
            pass

x = "+++++++++++++close_bd_mask+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[[[[[[[[[[[[[[[[[[[[++Ab_++++close_bd_mask++++++++++++++++++++++++++++++++++++++++++++++[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[+++++++++++++++[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[+++++++++++++close_bd_mask++++++++++++++++++++++++++++++++++++++++++++++[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[++Ab_++++close[[[[[[[[[[[[[[[[[[[++Ab_2W.s~pa2W.s~pa[[[[[[[[[[[[[[[[[[[[[[[[[[++Ab_2W.s~pa2W.s~pas"
dc = demoCls()
dc.demoFunc(x)
