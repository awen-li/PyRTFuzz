
from dis import *
import dis
import argparse
import io

API_TYPE_LIST = ['function']

def demoFunc(co):
    try:
        dis.show_code(co)
    except (AssertionError, AttributeError, LookupError, OSError, SyntaxError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError) as e:
        pass

demoFunc("QZElZzD((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((i@hi@YTv6m?zDi@h:")
