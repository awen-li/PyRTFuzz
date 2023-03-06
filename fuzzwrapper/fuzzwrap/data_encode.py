

import os
import io
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

def NullFunction ():
    pass

class DataProvider ():
    def __init__ (self, Depth=16):
        self.MaxDepth = Depth
        self.CurDepth = 0
        self.IsComplexType = False

    def RandomType (self, Excep=[]):
        Type = None
        while True:
            TypeIndex = random.randint(0, 10) #/*TypeLen-1*/
            Type = SuportTypes [TypeIndex]
            if not Type in Excep:
                break
        return Type

    def RandomStr (self, Length=16):
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

    def RandomList (self, Length=8):
        self.IsComplexType = True
        Length = random.randint(0, Length)
        List = []
        for i in range (0, Length):
            Type = self.RandomType ()
            Val = self.GetData (Type)
            #print ("### RandomList -> %s : %s" %(str(Type), str(Val)))
            List.append (Val)
        self.IsComplexType = False
        return List

    def RandomDict (self, Length=8):
        self.IsComplexType = True
        Length = random.randint(0, Length)
        Dict = {}
        for i in range (0, Length):
            Type = self.RandomType ()
            Val = self.GetData (Type)
            Key = self.RandomInt ()
            Dict [Key] = Val
        self.IsComplexType = False
        return Dict

    def RandomTuple (self, Length=8):
        RdList = self.RandomList (Length)
        return tuple (RdList)

    def RandomSet (self, Length=8):
        RdList = self.RandomList (Length)
        return set (RdList)

    def GenMemView (self, Str):
        Barry = bytearray(Str,'utf-8')
        return memoryview(Barry)
    
    def GenByteIo (self, Str):
        Bytes = bytes (Str, encoding='utf8')
        return io.BytesIO(Bytes)
    
    def GenStringIo (self, Str):
        return io.StringIO(Str)

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
            if self.IsComplexType == True:
                return self.GetData ('str')
            else:
                return self.RandomList ()
        elif type == 'memoryview':
            return self.GetData ('str')
        elif type == 'tuple':
            if self.IsComplexType == True:
                return self.GetData ('str')
            else:
                return self.RandomTuple ()
        elif type == 'dict':
            if self.IsComplexType == True:
                return self.GetData ('str')
            else:
                return self.RandomDict ()
        elif type == 'set':
            if self.IsComplexType == True:
                return self.GetData ('str')
            else:
                return self.RandomSet ()
        elif type == 'float':
            return self.RandomFloat ()
        elif type == 'function':
            return type
        elif type == 'Request':
            return type
        elif type == 'BytesIO':
            return self.GetData ('str')
        elif type == 'type':
            return self.RandomType ()
        elif type == 'Cookie':
            pass
        elif type == 'BufferedReader':
            pass
        elif type == 'StringIO':
            return self.GetData ('str')
        elif type == 'Element':
            pass
        elif type == 'EmailMessage':
            pass
        elif type == 'method':
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
        else:
            return b'None'
    
    def GetDataList (self, TypeList):
        ValueList = []
        for type in TypeList:
            Value = DataProvider ().GetData (type)
            ValueList.append (Value)
        return ValueList


_SPLITFLAG='%&$%'

def _Str2Value (Type, Value):  
    if Type in ['list', 'dict', 'tuple', 'set']:
        return eval (Value)
    elif Type == 'NoneType':
        return None
    elif Type == 'bytes':
        return bytes (Value, encoding='utf8')
    elif Type == 'memoryview':
        return DataProvider ().GenMemView (Value)
    elif Type == 'BytesIO':
        return DataProvider ().GenByteIo (Value)
    elif Type == 'StringIO':
        return DataProvider ().GenStringIo (Value)
    else:
        Type = eval (Type)
        return Type (Value)

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
        return _Str2Value (TypeList[0], ByteStream[4:])
    else:
        Values = ByteStream[4:].split (_SPLITFLAG)
        ValuseList = []
        TypeIndex  = 0
        for val in Values:
            print ("type = %s, value = %s " %(TypeList[TypeIndex], val))
            Value = _Str2Value (TypeList[TypeIndex], val)
            ValuseList.append (Value)
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
    
    def AssertDecode (self, DecodeValues, TypeList):
        if not isinstance (DecodeValues, tuple):
            DecodeValues = [DecodeValues]
        TypeIndex = 0
        for val in DecodeValues:
            self.AssertType (val, TypeList[TypeIndex])
            TypeIndex += 1

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

        TL = ['bytes', 'dict']
        ValueList = DataProvider ().GetDataList (TL)
        TypeList  = [v.__class__.__name__ for v in ValueList]
        self.AssertListEqual (TypeList, TL)

        # Encode test
        TypeList = ['int']
        Bytestream = PyEncode (TypeList)
        DecodeValues = PyDecode (TypeList, Bytestream)
        print ("\n### %s: Encode: %s, Decode:%s" %(str(TypeList), Bytestream, str(DecodeValues)))
        self.AssertDecode (DecodeValues, TypeList)
        
        TypeList = ['str', 'int', 'float', 'bool']
        Bytestream = PyEncode (TypeList)
        DecodeValues = PyDecode (TypeList, Bytestream)
        print ("\n### %s: Encode: %s, Decode:%s" %(str(TypeList), Bytestream, str(DecodeValues)))
        self.AssertDecode (DecodeValues, TypeList)

        TypeList = ['list']
        Bytestream = PyEncode (TypeList)
        DecodeValues = PyDecode (TypeList, Bytestream)
        print ("\n### %s: Encode: %s, Decode:%s" %(str(TypeList), Bytestream, str(DecodeValues)))
        self.AssertDecode (DecodeValues, TypeList)

        TypeList = ['list', 'int']
        Bytestream = PyEncode (TypeList)
        DecodeValues = PyDecode (TypeList, Bytestream)
        print ("\n### %s: Encode: %s, Decode:%s" %(str(TypeList), Bytestream, str(DecodeValues)))
        self.AssertDecode (DecodeValues, TypeList)

        TypeList = ['dict', 'tuple', 'bytes']
        Bytestream = PyEncode (TypeList)
        DecodeValues = PyDecode (TypeList, Bytestream)
        print ("\n### %s: Encode: %s, Decode:%s" %(str(TypeList), Bytestream, str(DecodeValues)))
        self.AssertDecode (DecodeValues, TypeList)

        TypeList = ['memoryview', 'tuple']
        Bytestream = PyEncode (TypeList)
        DecodeValues = PyDecode (TypeList, Bytestream)
        print ("### %s: Encode: %s, Decode:%s" %(str(TypeList), Bytestream, str(DecodeValues)))
        self.AssertDecode (DecodeValues, TypeList)

        TypeList = ['BytesIO', 'StringIO']
        Bytestream = PyEncode (TypeList)
        DecodeValues = PyDecode (TypeList, Bytestream)
        print ("### %s: Encode: %s, Decode:%s" %(str(TypeList), Bytestream, str(DecodeValues)))
        self.AssertDecode (DecodeValues, TypeList)
        