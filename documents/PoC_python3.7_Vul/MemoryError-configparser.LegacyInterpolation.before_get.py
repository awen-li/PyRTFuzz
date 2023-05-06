
from configparser import *
import configparser
import io
import re
from collections import OrderedDict

def demoFunc(value, vars):
    try:
        obj = configparser.LegacyInterpolation()
        print (value)
        print (vars)
        ret = obj.before_get("", "", "", value, vars)
    except (AssertionError, AttributeError, KeyError, LookupError, OSError, TypeError, ValueError, configparser.DuplicateOptionError, configparser.DuplicateSectionError, configparser.Error, configparser.InterpolationDepthError, configparser.InterpolationError, configparser.InterpolationMissingOptionError, configparser.InterpolationSyntaxError, configparser.MissingSectionHeaderError, configparser.NoOptionError, configparser.NoSectionError, configparser.ParsingError) as e:
        pass

demoFunc("%00000000000000000000000000004457664474921187ap??mj)lpX8%(aibRemmmmmmmmmmmmmlU]bus'", b'!@#$%^&*9523')
