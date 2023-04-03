import os
import sys
import socket
import time
from multiprocessing import Process
import atheris
from pygen import *
from platform import python_version

py_version = python_version()[0:3]

#######################################################################
#
# before fuzzing, instrument all runtimes
#
#######################################################################
def _InstrumentAll (ProbAll=True):
    if ProbAll == False:
        return
    
    with atheris.instrument_imports():
        import sqlite3
        import sqlite3.dbapi2
        import sqlite3.dump
        import html
        import html.entities
        import html.parser
        import ctypes
        import ctypes.wintypes
        import ctypes.util
        import ctypes.macholib.framework
        import ctypes.macholib.dyld
        import ctypes.macholib.dylib
        import xmlrpc
        import xmlrpc.client
        import xmlrpc.server
        import email
        import email.policy
        import email.message
        import email.utils
        import email.charset
        import email.feedparser
        import email.generator
        import email.parser
        import email.encoders
        import email.contentmanager
        import email.base64mime
        import email.headerregistry
        import email.header
        import email.iterators
        import email.errors
        import email.quoprimime
        import email.mime.nonmultipart
        import email.mime.message
        import email.mime.text
        import email.mime.application
        import email.mime.base
        import email.mime.audio
        import email.mime.image
        import email.mime.multipart
        import dbm
        import dbm.dumb
        import venv
        import wsgiref
        import wsgiref.handlers
        import wsgiref.validate
        import wsgiref.simple_server
        import wsgiref.headers
        import wsgiref.util
        import http
        import http.client
        import http.server
        import http.cookiejar
        import http.cookies
        import encodings
        import encodings.iso8859_14
        import encodings.cp858
        import encodings.cp1026
        import encodings.utf_16_be
        import encodings.aliases
        import encodings.cp850
        import encodings.cp1255
        import encodings.euc_jisx0213
        import encodings.mac_latin2
        import encodings.hp_roman8
        import encodings.mac_arabic
        import encodings.cp273
        import encodings.idna
        import encodings.cp1252
        import encodings.iso8859_9
        import encodings.cp869
        import encodings.iso2022_jp_1
        import encodings.gbk
        import encodings.mac_turkish
        import encodings.iso2022_jp_3
        import encodings.gb18030
        import encodings.zlib_codec
        import encodings.mac_greek
        import encodings.bz2_codec
        import encodings.cp874
        import encodings.iso2022_jp
        import encodings.raw_unicode_escape
        import encodings.utf_16
        import encodings.latin_1
        import encodings.ptcp154
        import encodings.cp864
        import encodings.cp1251
        import encodings.mac_farsi
        import encodings.cp950
        import encodings.cp852
        import encodings.cp1250
        import encodings.iso2022_jp_2
        import encodings.mac_roman
        import encodings.shift_jisx0213
        import encodings.big5hkscs
        import encodings.cp437
        import encodings.undefined
        import encodings.base64_codec
        import encodings.euc_jp
        import encodings.ascii
        import encodings.kz1048
        import encodings.utf_16_le
        import encodings.cp949
        import encodings.punycode
        import encodings.quopri_codec
        import encodings.cp862
        import encodings.iso8859_3
        import encodings.iso8859_11
        import encodings.cp1258
        import encodings.iso8859_4
        import encodings.cp037
        import encodings.cp1254
        import encodings.tis_620
        import encodings.utf_8_sig
        import encodings.cp1257
        import encodings.iso8859_13
        import encodings.utf_7
        import encodings.iso8859_6
        import encodings.johab
        import encodings.big5
        import encodings.cp857
        import encodings.shift_jis_2004
        import encodings.cp1256
        import encodings.shift_jis
        import encodings.iso2022_kr
        import encodings.cp1253
        import encodings.iso8859_15
        import encodings.utf_32_be
        import encodings.utf_32
        import encodings.palmos
        import encodings.unicode_escape
        import encodings.cp866
        import encodings.cp863
        import encodings.iso8859_7
        import encodings.koi8_t
        import encodings.iso8859_5
        import encodings.cp860
        import encodings.hz
        import encodings.cp861
        import encodings.rot_13
        import encodings.cp1125
        import encodings.cp1140
        import encodings.euc_kr
        import encodings.cp500
        import encodings.utf_32_le
        import encodings.cp865
        import encodings.iso8859_1
        import encodings.iso2022_jp_ext
        import encodings.koi8_r
        import encodings.iso8859_16
        import encodings.cp1006
        import encodings.mac_cyrillic
        import encodings.utf_8
        import encodings.mac_croatian
        import encodings.gb2312
        import encodings.euc_jis_2004
        import encodings.iso8859_10
        import encodings.iso2022_jp_2004
        import encodings.iso8859_2
        import encodings.cp720
        import encodings.cp855
        import encodings.koi8_u
        import encodings.charmap
        import encodings.uu_codec
        import encodings.mac_iceland
        import encodings.cp775
        import encodings.cp932
        import encodings.cp737
        import encodings.mac_romanian
        import encodings.hex_codec
        import encodings.cp856
        import encodings.cp424
        import encodings.cp875
        import encodings.iso8859_8
        import xml
        import xml.parsers.expat
        import xml.sax.expatreader
        import xml.sax.saxutils
        import xml.sax.xmlreader
        import xml.sax.handler
        import xml.dom.domreg
        import xml.dom.minidom
        import xml.dom.expatbuilder
        import xml.dom.NodeFilter
        import xml.dom.minicompat
        import xml.dom.pulldom
        import xml.dom.xmlbuilder
        import xml.etree.cElementTree
        import xml.etree.ElementTree
        import xml.etree.ElementInclude
        import xml.etree.ElementPath
        import ensurepip
        import pydoc_data
        import pydoc_data.topics
        import distutils
        import distutils.archive_util
        import distutils.text_file
        import distutils.versionpredicate
        import distutils.bcppcompiler
        import distutils.dep_util
        import distutils.cygwinccompiler
        import distutils.debug
        import distutils.filelist
        import distutils.extension
        import distutils.spawn
        import distutils.log
        import distutils.fancy_getopt
        import distutils.file_util
        import distutils.sysconfig
        import distutils.unixccompiler
        import distutils.util
        import distutils.config
        import distutils.cmd
        import distutils.core
        import distutils.version
        import distutils.errors
        import distutils.dist
        import distutils.dir_util
        import distutils.ccompiler
        import distutils.command.bdist_rpm
        import distutils.command.check
        import distutils.command.build_scripts
        import distutils.command.build
        import distutils.command.upload
        import distutils.command.build_clib
        import distutils.command.register
        import distutils.command.install
        import distutils.command.install_scripts
        import distutils.command.sdist
        import distutils.command.install_data
        import distutils.command.bdist
        import distutils.command.config
        import distutils.command.install_lib
        import distutils.command.bdist_dumb
        import distutils.command.clean
        import distutils.command.bdist_wininst
        import distutils.command.install_headers
        import distutils.command.install_egg_info
        import distutils.command.build_ext
        import distutils.command.build_py
        import logging
        import logging.handlers
        import logging.config
        import json
        import json.scanner
        import json.encoder
        import json.decoder
        import json.tool
        import collections
        import collections.abc
        import urllib
        import urllib.error
        import urllib.request
        import urllib.robotparser
        import urllib.parse
        import urllib.response

        import asyncio
        import asyncio.staggered
        import asyncio.unix_events
        import asyncio.tasks
        import asyncio.coroutines
        import asyncio.locks
        import asyncio.proactor_events
        import asyncio.events
        import asyncio.log
        import asyncio.base_tasks
        import asyncio.constants
        import asyncio.transports
        import asyncio.runners
        import asyncio.base_events
        import asyncio.trsock
        import asyncio.streams
        import asyncio.futures
        import asyncio.queues
        import asyncio.exceptions
        import asyncio.protocols
        import asyncio.sslproto
        import asyncio.selector_events
        import asyncio.format_helpers
        import asyncio.base_futures
        import operator
        import cgitb
        import cgi
        import compileall
        import imghdr
        import mailcap
        import opcode
        import random
        import ipaddress
        import tabnanny
        import getopt
        import textwrap
        import sunau
        import secrets
        import nturl2path
        import profile
        import gzip
        import calendar
        import smtplib
        import linecache
        import wave
        import optparse
        import site
        import shlex
        import filecmp
        import pathlib
        import webbrowser
        import aifc
        import formatter
        import gettext
        import imaplib
        import platform
        import chunk
        import mailbox
        import netrc
        import argparse
        import datetime
        import io
        import types
        import fnmatch
        import timeit
        import binhex
        import bisect
        import typing
        import ntpath
        import dataclasses
        import rlcompleter
        import weakref
        import os
        import fractions
        import tarfile
        import stringprep
        import dis
        import posixpath
        import pipes
        import sysconfig
        import asyncore
        import sndhdr
        import selectors
        import tempfile
        import queue
        import copy
        import bdb
        import zipfile
        import stat
        import pyclbr
        import keyword
        import modulefinder
        import pty
        import symtable
        import xdrlib
        import smtpd
        import cProfile
        import warnings
        import pickle
        import threading
        import asynchat
        import re
        import uu
        import shelve
        import telnetlib
        import socketserver
        import decimal
        import pickletools
        import fileinput
        import codecs
        import runpy
        import mimetypes
        import glob
        import configparser
        import symbol
        import cmd
        #import crypt
        import functools
        import imp
        import sre_compile
        import uuid
        import socket
        import ssl
        import quopri
        import getpass
        import pprint
        import difflib
        import statistics
        import nntplib
        import py_compile
        import sre_parse
        import abc
        import contextlib
        import signal
        import tty
        import copyreg
        import reprlib
        import contextvars
        import numbers
        import hashlib
        import tokenize
        import csv
        import sched
        import genericpath
        import hmac
        import zipapp
        import code
        import bz2
        import string
        import pkgutil
        import enum
        import lzma
        import sre_constants
        import pdb
        import plistlib
        import poplib
        import heapq
        import pstats
        import colorsys
        import base64
        import pydoc
        import codeop
        import zipimport
        import locale
        import ast
        import shutil
        import struct
        import token
        import ftplib
        if py_version == "3.9":
            import zoneinfo
            import tkinter
            import tkinter.commondialog
            import tkinter.colorchooser
            import tkinter.dialog
            import tkinter.messagebox
            import tkinter.constants
            import tkinter.tix
            import tkinter.scrolledtext
            import tkinter.simpledialog
            import tkinter.ttk
            import tkinter.dnd
            import tkinter.font
            import tkinter.filedialog
            import turtledemo
            import turtledemo.penrose
            import turtledemo.yinyang
            import turtledemo.forest
            import turtledemo.paint
            import turtledemo.nim
            import turtledemo.round_dance
            import turtledemo.peace
            import turtledemo.tree
            import turtledemo.two_canvases
            import turtledemo.planet_and_moon
            import turtledemo.chaos
            import turtledemo.clock
            import turtledemo.sorting_animate
            import turtledemo.bytedesign
            import turtledemo.fractalcurves
            import turtledemo.lindenmayer
            import turtledemo.rosette
            import turtledemo.minimal_hanoi
            import turtledemo.colormixer
            import asyncio.threads
            import curses
            import curses.ascii
            import curses.textpad
            import curses.panel
            import curses.has_key
            import graphlib




#######################################################################
#
# generate python application through send req to server
#
#######################################################################
SERVER_PORT = None

MSG_START_REQ="MSG_START_REQ"
MSG_START_ACK="MSG_START_ACK"

MSG_GENPY_REQ="MSG_GENPY_REQ"
MSG_GENPY_ACK="MSG_GENPY_ACK"

MSG_WEIGHT_REQ="MSG_WEIGHT_REQ"
MSG_WEIGHT_ACK="MSG_WEIGHT_ACK"

MSG_END="MSG_END"
MSG_ERR="MSG_ERR"

def _GetSocket ():
    if SERVER_PORT == None:
        raise Exception("Please specify port and init server first!")

    SrvAddress = ('localhost', SERVER_PORT)
    try:
        Socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    except OSError as msg:
        print ("Create socket with portfail: %s" %(msg))
        exit (0)
    
    while True:
        try:
            Socket.connect (SrvAddress)
            break
        except OSError as msg:
            #print ("Connect to server with port[%d] fail: %s" %(SERVER_PORT, msg))
            time.sleep (1)
            continue
    
    return Socket

def _DecodeMsg (Msg):
    MsgData = Msg.replace ('(', '')\
                 .replace (')', '')       
    Action, Data = MsgData.split (',')

    Action = Action.strip ()
    Data   = Data.strip ()
    if len (Action) == 0 or len (Data) == 0:
        return None, None
    return Action, Data

# "MSG_START_REQ:(hello,/path/apispec.xml)"
def _SendStartReq (SpecXml):
    Socket = _GetSocket ()

    Req = f"MSG_START_REQ:(hello,{SpecXml})"
    print ("[SendStartReq]" + Req)
    RepBytes = bytes(Req, 'utf-8')
    Socket.send (RepBytes)

    Ack = Socket.recv (1024).decode("utf-8") 
    Type, Data = Ack.split (':')
    if Type == MSG_ERR:
        print (Ack)
        sys.exit (0)
    else:
        _, Ret = _DecodeMsg (Data)
        return Ret

# "MSG_GENPY_REQ:(initial, /home/wen)|
#                (random, /home/wen)|
#                (specify, /home/wen)"
GEN_INITIAL = 'initial'
GEN_RANDOM  = 'random'
GEN_SPECIFY = 'specify'
def _SendGenReq (Action, Dir):
    Socket = _GetSocket ()

    Req = f"MSG_GENPY_REQ:({Action},{Dir})" 
    RepBytes = bytes(Req, 'utf-8')
    Socket.send (RepBytes)

    Ack = Socket.recv (1024).decode("utf-8") 
    Type, Data = Ack.split (':')
    if Type == MSG_ERR:
        print ("[SendGenReq]Error return:" + Ack)
        return ""
    else:
        _, Ret = _DecodeMsg (Data)
        return Ret

# "MSG_WEIGHT_REQ:(update, case)"
def _SendWeightedReq (Action, Case):
    Socket = _GetSocket ()

    Req = f"MSG_WEIGHT_REQ:({Action},{Case})"
    RepBytes = bytes(Req, 'utf-8')
    Socket.send (RepBytes)

    Ack = Socket.recv (1024).decode("utf-8") 
    Type, Data = Ack.split (':')
    if Type == MSG_ERR:
        return ""
    else:
        _, Ret = _DecodeMsg (Data)
        return Ret

# "MSG_END:(end,done)"
def _SendEndReq ():
    Socket = _GetSocket ()

    Req = "MSG_END:(end,done)"
    RepBytes = bytes(Req, 'utf-8')  
    Socket.send (RepBytes)

"""
Interface: generate initial seeds for fuzzing
"""
def GetInitialSeeds (Dir):
    if not os.path.exists (Dir):
        os.mkdir (Dir)
    
    DoneFlag = Dir+'/initial_done'
    if os.path.exists (DoneFlag):
        print ("Initialization is already done!")
        return 'done'
    else:
        Ret = _SendGenReq (GEN_INITIAL, Dir)
        if Ret == 'done':
            with open (DoneFlag, 'w'):
                pass
        return Ret

"""
Interface: generate a random seed for fuzzing
"""
def GetRandomSeed (Dir):
    return _SendGenReq (GEN_RANDOM, Dir)

"""
Interface: generate a seed of specified run-time API for fuzzing
"""
def GetSpecifiedSeed (Case):
    return _SendGenReq (GEN_SPECIFY, Case)

"""
Interface: generate a seed of specified run-time API for fuzzing
"""
def UpdateWeight (Case):
    return _SendWeightedReq ('update', Case)

"""
Interface: inform the server to end
"""
def Done ():
    _SendEndReq ()
    time.sleep (1)


#######################################################################
#
# setup app gen server
#
#######################################################################
"""
Individual process: python application generation service for fuzzing
"""
def _StartPyGenServer (Port):
    CS = CodeServer (Port)
    CS.Start ()

def SetupPyFuzz (ApiSpecXml, Port, ProbAll=True):
    global SERVER_PORT
    SERVER_PORT = Port

    if not os.path.exists (ApiSpecXml):
        print ("Can not find %s, please copy it to current directory!" %ApiSpecXml)
        sys.exit (0)

    # 1. setup the python app generator
    server = Process(target=_StartPyGenServer, args=(Port,))
    server.start()
    
    _SendStartReq (ApiSpecXml)

    # 2. instrument all python runtimes
    _InstrumentAll (ProbAll)
    return True