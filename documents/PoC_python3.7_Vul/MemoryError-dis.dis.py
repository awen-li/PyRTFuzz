
from dis import *
import dis
import argparse
import io

def demoFunc(x):
    try:
        dis.dis(x)
    except (AssertionError, AttributeError, LookupError, OSError, SyntaxError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError) as e:
        pass

x = 'F-((((((((((Fals((als((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((t#'
demoFunc(x)
