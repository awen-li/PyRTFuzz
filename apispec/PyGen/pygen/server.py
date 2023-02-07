import sys
import socket
import traceback
from .script import CodeGen

class PyMsg ():
    MSG_START_REQ="MSG_START_REQ"
    MSG_START_ACK="MSG_START_ACK"

    MSG_GENPY_REQ="MSG_GENPY_REQ"
    MSG_GENPY_ACK="MSG_GENPY_ACK"

    MSG_WEIGHT_REQ="MSG_WEIGHT_REQ"
    MSG_WEIGHT_ACK="MSG_WEIGHT_ACK"

    MSG_END="MSG_END"
    MSG_ERR="MSG_ERR"

    def __init__ (self, Socket):
        self.MsgHandler = {}
        self.InitMsgHandle ()

        self.Socket = Socket
        self.Generator = None

    def InitMsgHandle (self):
        self.MsgHandler[PyMsg.MSG_START_REQ] = self.HandleStartReq
        self.MsgHandler[PyMsg.MSG_GENPY_REQ] = self.HandleGenPyReq
        self.MsgHandler[PyMsg.MSG_WEIGHT_REQ] = self.HandleWeightReq
        self.MsgHandler[PyMsg.MSG_END] = self.HandleEnd
    
    def MsgSend (self, Msg):
        self.Socket.send (Msg)

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
    def HandleStartReq (self, data):
        Action, SpecPath = self.DecodeMsg (data)
        if Action == None or SpecPath == None:
            return None
        
        if Action != 'hello':
            self.MsgSend (PyMsg.MSG_GENPY_ACK+":(hello, unknown action)")
            return None

        Generator = CodeGen (SpecPath)
        if not Generator.IsCoreUp ():
            self.MsgSend (PyMsg.MSG_GENPY_ACK+":(hello, core start fail with " + SpecPath + ")")
            return None
        self.Generator = Generator

        return (PyMsg.MSG_GENPY_ACK+":(hello, done)")
    
    # "MSG_GENPY_REQ:(initial, /home/wen)|
    #                (random, /home/wen)|
    #                (weighted, /home/wen)"
    def HandleGenPyReq (self, data):
        if self.Generator == None:
            self.MsgSend (PyMsg.MSG_ERR+":(error, Server has not been initialized yet!)")
            return None

        Action, Dir = self.DecodeMsg (data)
        if Action == None or Dir == None:
            return None

        if Action == 'initial':
            self.Generator.GenInitPy (Dir)
            return (PyMsg.MSG_GENPY_ACK+":(initial, done)")
        elif Action == 'random':
            self.Generator.GenRandomPy (Dir)
            return (PyMsg.MSG_GENPY_ACK+":(random, done)")
        elif Action == 'weighted':
            self.Generator.GenWeightedPy (Dir)
            return (PyMsg.MSG_GENPY_ACK+":(weighted, done)")
        else:
            return (PyMsg.MSG_ERR+":(error, unknow action for MSG_GENPY_REQ)")

    
    # "MSG_WEIGHT_REQ:(update, case)"
    def HandleWeightReq (self, data):
        if self.Generator == None:
            self.MsgSend (PyMsg.MSG_ERR+":(error, Server has not been initialized yet!)")
            return None
        
        Action, Case = self.DecodeMsg (data)
        if Action == None or Case == None:
            return None

        if Action == 'update':
            self.Generator.UpdateWeight (Case)
        else:
            return (PyMsg.MSG_ERR+":(error, unknow action for MSG_WEIGHT_REQ)")

    # "MSG_END:(end,)"
    def HandleEnd (self, data):
        self.Socket.close ()
        sys.exit (0)

    def Handle (self, MsgBuf):
        MsgType, MsgData = MsgBuf.split (':')
        MsgHandle = self.MsgHandler.get (MsgType)
        if MsgHandle == None:
            return None
        return MsgHandle (MsgData)

class CodeServer ():
    def __init__ (self, Port):
        self.Port = Port
        self.Socket = self.InitServer ()
        self.MsgColver = PyMsg (self.Socket)

    def InitServer (self):
        Address = ("", self.Port)
        Socket = socket.socket (socket.AF_INET, socket.SOCKK_STREAM)
        Socket.bind (Address)
        Socket.listen (1)
        return Socket

    def OneConnect (self, in_connection, in_address):
        try:
            RevBuf = in_connection.recv (1024)
            SendBuf = self.MsgColver.Handle (RevBuf)
            if SendBuf != None:
                self.MsgSend (SendBuf)
            else:
                print ("Process msg[%s] fail!", str(RevBuf))
                pass
        except KeyboardInterrupt:
                raise
        except:
            traceback.print_exc ()
            pass

    def Start (self):
        while True:
            try:
                in_connection, in_address = self.Socket.accept ()
            except KeyboardInterrupt:
                raise
            except:
                traceback.print_exc ()
                continue

            self.OneConnect (in_connection, in_address)


