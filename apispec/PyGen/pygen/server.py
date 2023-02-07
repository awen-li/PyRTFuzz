import socket
import traceback
from .script import CodeGen

class PyMsg ():
    def __init__ (self, MsgBuf):
        pass

    def Handle (self):
        pass


class CodeServer ():
    def __init__ (self, Port):
        self.Port = Port
        self.Socket = None

    def InitServer (self):
        Address = ("", self.Port)
        Socket = socket.socket (socket.AF_INET, socket.SOCKK_STREAM)
        Socket.bind (Address)
        Socket.listen (1)
        return Socket

    def OneConnect (self, in_connection, in_address):
        try:
            RevBuf = in_connection.recv (1024)
            RevMsg = PyMsg (RevBuf)
            SendBuf = RevMsg.Handle ()
            self.Socket.send (SendBuf)
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


