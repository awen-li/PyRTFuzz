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

    def __init__ (self):
        self.MsgHandler = {}
        self.InitMsgHandle ()

    def InitMsgHandle (self):
        self.MsgHandler[PyMsg.MSG_START_REQ] = self.HandleStartReq
        self.MsgHandler[PyMsg.MSG_GENPY_REQ] = self.HandleGenPyReq
        self.MsgHandler[PyMsg.MSG_WEIGHT_REQ] = self.HandleWeightReq
        self.MsgHandler[PyMsg.MSG_END] = self.HandleEnd

    # "MSG_START_REQ:(hello,)"
    def HandleStartReq (self, data):
        return (PyMsg.MSG_GENPY_ACK+":(hello,)")
    
    # "MSG_GENPY_REQ:(initialization, /home/wen)|
    #                (random, /home/wen)|
    #                (weighted, /home/wen)"
    def HandleGenPyReq (self, data):
        pass
    
    # "MSG_WEIGHT_REQ:(update,libname, modulename, apiname)"
    def HandleWeightReq (self, data):
        pass

    # "MSG_END:(end,)"
    def HandleEnd (self, data):
        pass

    def Handle (self, MsgBuf):
        MsgType, MsgData = MsgBuf.split (':')
        MsgHandle = self.MsgHandler.get (MsgType)
        if MsgHandle == None:
            return None
        return MsgHandle (MsgData)

class CodeServer ():
    def __init__ (self, Port):
        self.Port = Port
        self.Socket = None
        self.MsgColver = PyMsg ()

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
                self.Socket.send (SendBuf)
            else:
                print ("Process msg[%s] fail!", str(RevBuf))
        except KeyboardInterrupt:
                raise
        except:
            traceback.print_exc ()
            pass

    def Start (self):
        self.Socket = self.InitServer ()
        while True:
            try:
                in_connection, in_address = self.Socket.accept ()
            except KeyboardInterrupt:
                raise
            except:
                traceback.print_exc ()
                continue

            self.OneConnect (in_connection, in_address)


