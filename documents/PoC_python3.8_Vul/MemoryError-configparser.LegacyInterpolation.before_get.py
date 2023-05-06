
from configparser import *
import configparser
import io
import re

def demoFunc(value, vars):
    try:
        parser = configparser.ConfigParser()
        parser['DEFAULT'] = {'ServerAliveInterval': '45',
                             'Compression': 'yes',
                             'CompressionLevel': '9'}

        obj = configparser.LegacyInterpolation()
        ret = obj.before_get(parser, "", "", value, vars)
    except (AssertionError, AttributeError, KeyError, LookupError, OSError, TypeError, ValueError, configparser.DuplicateOptionError, configparser.DuplicateSectionError, configparser.Error, configparser.InterpolationDepthError, configparser.InterpolationError, configparser.InterpolationMissingOptionError, configparser.InterpolationSyntaxError, configparser.MissingSectionHeaderError, configparser.NoOptionError, configparser.NoSectionError, configparser.ParsingError) as e:
        pass

value = "*yFqf0GcXyVkF6jQbv-ts' et,50664202cleanse_cr!ash6: @'zD&0P'OfrJKLvtwDx14x?325@a2n87xXXEzqOgy8aKSx4*mK6E*hATBjxCA)B#iptlBd3O4TU&*zaaM@a2n87xXXEzqOg31571263: 'www.python.org', 49529868: 'OfrJKLvtwDx14Ru0eIp)lAg9JE)hV0kf1wt$F9U2V!JR*xz9M5rx0A325XPly1DhtDdseI$^#Fa%7777777777777777777handle_usr177777777777777777777777777777777777BJ', 1750 2910921: 51'www.python.org', 2~3mergee_allocator_interval60745__getitem__ 34951?40??33: '/tmp/fu'zzing-test', 506642888882JOGu+%DkAVU1)g331XIB)@#YP0ZzJwdtS*9RsWtL%(tw4G^WDcGVh59cFXMkh4i1gParser"
vars = {"*yFqf0GcXyVkF6jQ&M@a2n87xX551607453: 'oAy9K'crash7: 'zDCAuuaBL8)B#iptlBUoWCt4Z#5IK&zSxqmfxJhcross_overZmVLbn1P5uQ\x00\x00\x00\x016JRsM2T%Mkh4i10Z*52"}
        
demoFunc(value, vars)
