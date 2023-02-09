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

    def __init__ (self, MsgSend, ShutDown):
        self.MsgHandler = {}
        self.InitMsgHandle ()

        self.MsgSend  = MsgSend
        self.ShutDown = ShutDown
        self.Generator = None

    def InitMsgHandle (self):
        self.MsgHandler[PyMsg.MSG_START_REQ] = self.HandleStartReq
        self.MsgHandler[PyMsg.MSG_GENPY_REQ] = self.HandleGenPyReq
        self.MsgHandler[PyMsg.MSG_WEIGHT_REQ] = self.HandleWeightReq
        self.MsgHandler[PyMsg.MSG_END] = self.HandleEnd
    
    def DecodeMsg (self, Msg):
        MsgData = Msg.replace ('(', '')\
                     .replace (')', '')       
        Action, Data = MsgData.split (',')

        Action = Action.strip ()
        Data   = Data.strip ()
        if len (Action) == 0 or len (Data) == 0:
            self.MsgSend (PyMsg.MSG_ERR+":(error,empty field)")
            return None, None
        print ("[DecodeMsg]Action = %s, Data = %s" %(Action, Data))
        return Action, Data

    # "MSG_START_REQ:(hello,/path/apispec.xml)"
    def HandleStartReq (self, data):
        Action, SpecPath = self.DecodeMsg (data)
        if Action == None or SpecPath == None:
            print ("[HandleStartReq]DecodeMsg fail: %s - %s" %(str(Action), str(SpecPath)))
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
            Case = self.Generator.GenRandomPy (Dir)
            return (PyMsg.MSG_GENPY_ACK + f":(random, {Case})")
        elif Action == 'weighted':
            Case = self.Generator.GenWeightedPy (Dir)
            return (PyMsg.MSG_GENPY_ACK + f":(weighted, {Case})")
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
            return (PyMsg.MSG_WEIGHT_ACK+":(update, done)")
        else:
            return (PyMsg.MSG_ERR+":(error, unknow action for MSG_WEIGHT_REQ)")

    # "MSG_END:(end,)"
    def HandleEnd (self, data):
        self.ShutDown ()

    def Handle (self, MsgBuf):
        MsgType, MsgData = MsgBuf.split (':')
        print ("[Handle](MsgType, MsgData) = (%s, %s)" %(MsgType, MsgData))
        MsgHandle = self.MsgHandler.get (MsgType)
        if MsgHandle == None:
            return None
        return MsgHandle (MsgData)

class CodeServer ():
    def __init__ (self, Port):
        self.Port      = Port
        self.Socket    = self.InitServer ()
        self.InSocket  = None
        self.MsgColver = PyMsg (self.MsgSend, self.ShutDown)

    def MsgSend (self, Msg):
        Msg = bytes(Msg, 'utf-8')
        self.InSocket.send (Msg)

    def ShutDown (self):
        self.Socket.close ()
        self.InSocket.close ()
        sys.exit (0)

    def InitServer (self):
        Address = ("", self.Port)
        try:
            Socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        except OSError as msg:
            print ("Create socket with fail: %s" %(msg))
            exit (0)
        
        try:
            Socket.bind (Address)
            Socket.listen (1)
        except OSError as msg:
            Socket.close()
            print ("Bind socket with port[%d] fail: %s" %(self.Port, msg))
            exit (0)
        
        return Socket

    def OneConnect (self, InSocket, InAddress):
        self.InSocket = InSocket
        try:
            RevBuf = InSocket.recv (1024).decode("utf-8") 
            SendBuf = self.MsgColver.Handle (RevBuf)
            if SendBuf != None:
                self.MsgSend (SendBuf)
                self.InSocket.close ()
                self.InSocket = None
            else:
                print ("Process msg[%s] fail!" %str(RevBuf))
                self.InSocket.close ()
                self.InSocket = None
        except OSError as msg:
            self.InSocket.close ()
            self.InSocket = None
            traceback.print_exe ()
        except:
            self.InSocket.close ()
            self.InSocket = None

    def Start (self):
        while True:
            try:
                InSocket, InAddress = self.Socket.accept ()
            except:
                break

            self.OneConnect (InSocket, InAddress)


