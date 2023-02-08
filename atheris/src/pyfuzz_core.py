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

def DecodeMsg (self, Msg):
    MsgData = Msg.replace ('(', '')\
                 .replace (')', '')       
    Action, Data = MsgData.split (',')

    Action = Action.strip ()
    Data   = Data.strip ()
    if len (Action) == 0 or len (Data) == 0:
        self.MsgSend (PyMsg.MSG_ERR+":(error,empty field)")
        return None, None
    return Action, Data

# "MSG_START_REQ:(hello,/path/apispec.xml)"
def _SendStartReq (SpecXml):
    req = f"MSG_START_REQ:(hello,{SpecXml})"

    Socket = _GetSocket ()

    Socket.send (req)
    ack = Socket.recv (1024)
    Type, Data = Ack.split (':')
    if Type == MSG_ERR:
        print (ack)
        sys.exit (0)

# "MSG_GENPY_REQ:(initial, /home/wen)|
#                (random, /home/wen)|
#                (weighted, /home/wen)"
def SendGenReq (Action, Dir):
    req = f"MSG_START_REQ:({Action},{Dir})"

    Socket = _GetSocket () 
    Socket.send (req)

    Ack = Socket.recv (1024)
    Type, Data = Ack.split (':')
    if Type == MSG_ERR:
        return ""

    _, Case = DecodeMsg (Data)
    if Action == 'initial':
        return
    elif Action == 'random':
        return Case
    elif Action == 'weighted':
        return Case
    else:
        return ""

# "MSG_WEIGHT_REQ:(update, case)"
def SendWeightedReq (Action, Case):
    req = f"MSG_START_REQ:({Action},{Case})"

    Socket = _GetSocket ()  
    Socket.send (req)

    Ack = Socket.recv (1024)
    Type, Data = Ack.split (':')
    if Type == MSG_ERR:
        return
    else:
        pass

# "MSG_END:(end,)"
def SendEndReq ():
    req = "MSG_END:(end,)"
    Socket = _GetSocket ()  
    Socket.send (req)


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