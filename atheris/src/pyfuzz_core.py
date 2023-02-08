# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Two-level fuzzing for python interpreter and runtime libraries"""

import sys
import socket
from multiprocessing import Process
from .import_hook import instrument_imports
from pygen import *

#######################################################################
#
# before fuzzing, instrument all runtimes
#
#######################################################################
def _InstrumentAll ():
    with instrument_imports():
        import quopri



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
            Socket.close()
            print ("Connect to server with port[%d] fail: %s" %(SERVER_PORT, msg))
            continue
    
    return Socket

def SendMsg (Socket, Msg):
    pass

def RecvMsg (Socket, Msg):
    pass

def _SendStartReq (SpecXml):
    req = f"MSG_START_REQ:(hello,{SpecXml})"

    Socket = _GetSocket ()
    SendMsg (Socket, req)

    ack = RecvMsg (Socket)
    print (ack)

def PyMutation ():
    pass
    

#######################################################################
#
# setup app gen server
#
#######################################################################
def _StartPyGenServer (Port):
    CS = CodeServer (Port)
    CS.Start ()

def SetupPyFuzz (Port=19163):
    SERVER_PORT = Port

    # 1. setup the python app generator
    server = Process(target=_StartPyGenServer, args=(Port,))
    server.start()
    _SendStartReq ()

    # 2. instrument all python runtimes
    _InstrumentAll ()