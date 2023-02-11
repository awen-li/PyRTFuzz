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

import os
import sys
import socket
import time
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
        return
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

def SetupPyFuzz (ApiSpecXml, Port=19163):
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
    _InstrumentAll ()
    return True