
from dis import *
import dis
import argparse
import io

def demoFunc(arg):
    try:
        ret = dis.code_info(x)
    except (AssertionError, AttributeError, LookupError, OSError, SyntaxError, TypeError, ValueError, argparse.ArgumentError, argparse.ArgumentTypeError) as e:
        pass

x = "_OOiaKIdelmerg8>efl_l%ak-print_fiNWI8plRKImJt_cuhfsr23f8>l>l_l%aksaksr22fdata_flow_tracel>l_l%aksr22f8>l0x^d[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[c-_l%aksr22f8hDKImJc-print_ignore_oomsI[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[c-_l%aksr22f8hfinSQQ''"
demoFunc(x)
