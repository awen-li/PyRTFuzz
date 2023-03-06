

import os
import sys
import random

SuportTypes = ['str', 'int', 'bool', 'bytes', 'NoneType', 'list', 'dict', 'tuple', 'memoryview', 'function', 
               'float', 'Request', 'BytesIO', 'Mock', 'type', 'C', 'builtin_function_or_method', 'StringIO', 
               'object', 'BufferedReader', 'Cookie', '_UnixSelectorEventLoop', 'Element', 'EmailMessage', 
               'EnumMeta', 'coroutine', 'complex', 'FakePath', 'method', 'method-wrapper', 'ConfigParser', 
               'Message', 'LogRecord', 'AddressFamily', 'socket', 'HTTPResponse', 'HTTPMessage', 'range', 
               'BufferedWriter', 'Module', 'SSLContext', 'TextIOWrapper', 'set', 'SocketKind', 'PlistFormat', 
               'Fault', 'datetime', 'generator', 'Match', 'XMLParser', 'frame', 'BadIterable', 'PosixPath', 
               'IPv4Address', 'code', '_SSLMethod', 'Constant', 'Expression', 'Marshaller', 'ClassWithAnnotation', 
               '_UniqueAddressHeader', 'MIMEApplication', 'MIMEText', 'FakeResponse', 'AttributesImpl', 
               'UnixCCompiler', 'Extension', 'MockFile', 'TestLoop', 'Future', '_SentinelObject', 'Option', 
               'FakeTimer', '_MISSING_TYPE', 'echo_client', 'Pattern', 'RawConfigParser', 'ChainMap', 'module', 
               'UUID', 'MemoryBIO', 'Purpose', 'TLSVersion', 'VerifyMode', 'frozenset', 'Signals', 'stat_result', 
               'Template', 'TestCgitb', 'TestInstance', 'MIMEImage', 'DefaultCookiePolicy', 'InputSource', 
               'SAXParseException', 'ExpatLocator', 'Text', 'DocumentType', 'Document', 'Attr', 'AttributesNSImpl', 
               'SAXExerciser', '_SelectorContext', 'OSError', 'MockRaceConditionHandler', 'JSONDecoder', 'ProxyHandler', 
               'MockHTTPClass', 'MockResponse', 'FakeSocket', 'OpenerDirector', 'filter', 'ValueError', 'AddressInfo', 
               '_Sentinel', 'SafeChildWatcher', 'DummyExecutor', '_SelectorSocketTransport', 'TaskWakeupMethWrapper', 
               'Context', 'RuntimeError', 'SSLCertVerificationError', '_sunau_params', 'fake_frame', 'struct_time', 
               '_wave_params', 'Values', 'OptionParser', 'IndentedHelpFormatter', 'ExampleBrowser', 'TestProgram', 
               'ZoneInfo', '_ProtocolMeta', 'ABCMeta', 'SourceFileLoader', 'SimpleNameSpace', 'A', '_Stream', 
               'traceback', 'SendfileTestServer', 'st', 'ZipInfo', 'UserWarning', 'IdleConfParser', 'Session', 
               'Options', 'VerifyFlags', 'NormalDist', 'date', 'PycInvalidationMode', 'SubPattern', 'Tokenizer', 
               'TestCM', 'AsyncExitStack', 'array', 'deque', 'Event', 'Vec2D', 'zipimporter', 'itemgetter', 'Profile', 
               '_PlainTextDoc', 'Call', '_SocketWriter']

TypeLen = len (SuportTypes)

class DataProvider ():
    def __init__ (self, Depth=32):
        self.MaxDepth = Depth
        self.CurDepth = 0

    def RandomType (self, Excep=[]):
        Type = None
        while True:
            TypeIndex = random.randint(0, 10) #/*TypeLen-1*/
            Type = SuportTypes [TypeIndex]
            if not Type in Excep:
                break
        return Type

    def RandomStr (self, Length=256):
        Length = random.randint(0, Length)
        StrCtx = ''
        for i in range (0, Length):
            StrCtx += random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMabcdefghijklmnopqrstuvwxyz!@#$%^&*()')
        return StrCtx

    def RandomInt (self, Value=4294967295):
        return random.randint(0, Value)

    def RandomBool (self):
        rd = random.randint(0, 2)
        if rd == 1:
            return True
        else:
            return False

    def RandomFloat (self, Value=4294967295):
        return random.uniform(0, Value)

    def RandomBytes (self):
        Str = self.RandomStr ()
        return bytes (Str, encoding='utf8')

    def RandomList (self, Length=256):
        Length = random.randint(0, Length)
        List = []
        for i in range (0, Length):
            Type = self.RandomType ()
            Val = self.GetData (Type)
            List.append (Val)
        return List

    def RandomDict (self, Length=256):
        Length = random.randint(0, Length)
        Dict = {}
        for i in range (0, Length):
            Type = self.RandomType ()
            Val = self.GetData (Type)
            Key = self.RandomInt ()
            Dict [Key] = Val
        return Dict

    def RandomTuple (self, Length=256):
        RdList = self.RandomList (Length)
        return tuple (RdList)

    def RandomSet (self, Length=256):
        RdList = self.RandomList (Length)
        return set (RdList)

    def RandomMemView (self):
        RdStr = self.RandomStr ()
        Barry = bytearray(RdStr,'utf-8')
        return memoryview(Barry)

    def GetData (self, type):
        self.CurDepth += 1
        if self.CurDepth >= self.MaxDepth:
            return None
        
        if type == 'NoneType':
            TypeIndex = random.randint(0, TypeLen-1)
            if TypeIndex%2 == 0:
                return None
            else:
                return self.GetData (SuportTypes [TypeIndex])
        elif type == 'str':
            return self.RandomStr ()
        elif type == 'int':
            return self.RandomInt ()
        elif type == 'bool':
            return self.RandomBool ()
        elif type == 'bytes':
            return self.RandomBytes ()
        elif type == 'list':
            return self.RandomList ()
        elif type == 'memoryview':
            return self.RandomMemView ()
        elif type == 'tuple':
            return self.RandomTuple ()
        elif type == 'dict':
            return self.RandomDict ()
        elif type == 'float':
            return self.RandomFloat ()
        elif type == 'function':
            pass
        elif type == 'Request':
            pass
        elif type == 'BytesIO':
            pass
        elif type == 'type':
            pass
        elif type == 'builtin_function_or_method':
            pass
        elif type == 'Mock':
            pass
        elif type == 'C':
            pass
        elif type == 'Cookie':
            pass
        elif type == 'BufferedReader':
            pass
        elif type == 'object':
            pass
        elif type == 'StringIO':
            pass
        elif type == 'Element':
            pass
        elif type == 'EmailMessage':
            pass
        elif type == 'method':
            pass
        elif type == '_UnixSelectorEventLoop':
            pass
        elif type == 'EnumMeta':
            pass
        elif type == 'coroutine':
            pass
        elif type == 'complex':
            pass
        elif type == 'method-wrapper':
            pass
        elif type == 'ConfigParser':
            pass
        elif type == 'set':
            pass
        else:
            pass
    
    def GetDataList (self, TypeList):
        ValueList = []
        for type in TypeList:
            Value = DataProvider ().GetData (type)
            ValueList.append (Value)
        return ValueList


_SPLITFLAG='%&$%'

def PyEncode (TypeList):
    ValueList = DataProvider ().GetDataList (TypeList)
    ByteStream = _SPLITFLAG + _SPLITFLAG.join ([str(value) for value in ValueList])
    return ByteStream


def PyDecode (TypeList, ByteStream):
    if ByteStream[0:4] != _SPLITFLAG:
        return ByteStream
    
    TypeNum = len (TypeList)
    if TypeNum == 0:
        return ByteStream[4:]
    
    if len (TypeList) == 1:
        Type = eval (TypeList[0])
        return Type(ByteStream[4:])
    else:
        Values = ByteStream[4:].split (_SPLITFLAG)
        ValuseList = []
        TypeIndex  = 0
        for val in Values:
            Type = eval (TypeList[TypeIndex])
            ValuseList.append (Type(val))
            TypeIndex += 1
        return tuple (ValuseList)
    

class DataProviderTest ():
    def AssertType (self, Value, Type):
        if Value.__class__.__name__ != Type:
            print ("### [TypeAssert] Value type: %s, expected: %s" %(Value.__class__.__name__, Type))
            return False
        else:
            print ("### [TypeAssert] Value type: %s success" %(Type))
            return True
        
    def AssertListEqual (self, SList, DList):
        if len (SList) != len (DList):
            print ("AssertListEqual Fail: SList = %s while DList = %s" %(str(SList), str(DList)))
            return False
        else:
            for s in SList:
                if not s in DList:
                    print ("AssertListEqual Fail: SList = %s while DList = %s" %(str(SList), str(DList)))
                    return False
            
            for d in DList:
                if not d in SList:
                    print ("AssertListEqual Fail: SList = %s while DList = %s" %(str(SList), str(DList)))
                    return False
                
            print ("AssertListEqual Success on TypeList: %s" %(str(SList)))
            return True

    def TestEntry (self):
        # single type testing
        self.AssertType (DataProvider ().RandomStr (), 'str')
        self.AssertType (DataProvider ().RandomInt (), 'int')
        self.AssertType (DataProvider ().RandomBool (), 'bool')
        self.AssertType (DataProvider ().RandomFloat (), 'float')
        self.AssertType (DataProvider ().RandomBytes (), 'bytes')
        self.AssertType (DataProvider ().RandomList (), 'list')
        self.AssertType (DataProvider ().RandomDict (), 'dict')
        self.AssertType (DataProvider ().RandomTuple (), 'tuple')
        self.AssertType (DataProvider ().RandomMemView (), 'memoryview')

        # multiple type testing
        TL = ['str', 'int']
        ValueList = DataProvider ().GetDataList (TL)
        TypeList  = [v.__class__.__name__ for v in ValueList]
        self.AssertListEqual (TypeList, TL)

        TL = ['str', 'int', 'float', 'bool']
        ValueList = DataProvider ().GetDataList (TL)
        TypeList  = [v.__class__.__name__ for v in ValueList]
        self.AssertListEqual (TypeList, TL)

        TL = ['bytes', 'list', 'tuple']
        ValueList = DataProvider ().GetDataList (TL)
        TypeList  = [v.__class__.__name__ for v in ValueList]
        self.AssertListEqual (TypeList, TL)

        TL = ['memoryview', 'dict']
        ValueList = DataProvider ().GetDataList (TL)
        TypeList  = [v.__class__.__name__ for v in ValueList]
        self.AssertListEqual (TypeList, TL)

        # Encode test
        TypeList = ['int']
        Bytestream = PyEncode (TypeList)
        DecodeValues = PyDecode (TypeList, Bytestream)
        print ("### %s: Encode: %s, Decode:%d" %(str(TypeList), Bytestream, DecodeValues))
        self.AssertType (DecodeValues, TypeList[0])
        
        TypeList = ['str', 'int', 'float', 'bool']
        Bytestream = PyEncode (TypeList)
        DecodeValues = PyDecode (TypeList, Bytestream)
        print ("### %s: Encode: %s, Decode:%s" %(str(TypeList), Bytestream, str(DecodeValues)))
        TypeIndex = 0
        for val in DecodeValues:
            self.AssertType (val, TypeList[TypeIndex])
            TypeIndex += 1
