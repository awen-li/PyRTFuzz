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
import random

SuportTypes = ['NoneType', 'str', 'int', 'bool', 'bytes', 'list', 'memoryview', 'tuple', 'dict', 'float', 
               'function', 'Request', 'BytesIO', 'type', 'builtin_function_or_method', 'Mock', 'C', 'Cookie', 'BufferedReader', 'object', 
               'StringIO', 'Element', 'EmailMessage', 'method', '_UnixSelectorEventLoop', 'EnumMeta', 'coroutine', 'complex', 'method-wrapper', 'ConfigParser', 
               'FakePath', 'Message', 'LogRecord', 'Module', 'HTTPResponse', 'HTTPMessage', 'BufferedWriter', 'module', 'range', 'TextIOWrapper', 
               'set', 'SocketKind', 'socket', 'generator', 'Match', 'frame', 'code', 'AddressFamily', '_SSLMethod', 'PosixPath', 
               'Constant', 'Marshaller', 'datetime', 'ClassWithAnnotation', 'MIMEApplication', 'FakeResponse', 'AttributesImpl', 'UnixCCompiler', 'Extension', 'MockFile', 
               'Future', 'Option', 'FakeTimer', '_MISSING_TYPE', 'Pattern', 'RawConfigParser', 'ChainMap', 'UUID', 'MemoryBIO', 'Purpose', 
               'frozenset', 'Signals', 'stat_result', 'Template', 'PlistFormat', 'TestCgitb', 'Expression', 'Fault', 'TestInstance', '_ContentTypeHeader', 
               '_UniqueAddressHeader', 'MIMEImage', 'MIMEText', 'DefaultCookiePolicy', 'InputSource', 'SAXParseException', 'ExpatLocator', 'Text', 'Document', 
               'Attr', 'AttributesNSImpl', '_SelectorContext', 'OSError', 'MockRaceConditionHandler', 'JSONDecoder', 'ProxyHandler', 'MockHTTPClass', 'MockResponse', 
               'FakeSocket', 'OpenerDirector', 'filter', 'ValueError', 'TestLoop', 'SafeChildWatcher', 'DummyExecutor', '_SelectorSocketTransport', 'TaskWakeupMethWrapper', 
               'Context', 'RuntimeError', '_sunau_params', 'fake_frame', 'struct_time', 'SSLContext', '_wave_params', 'Values', 'OptionParser', 'IndentedHelpFormatter', 
               'TestProgram', '_ProtocolMeta', 'ABCMeta', 'SourceFileLoader', 'A', 'RefCycle', '_Stream', 'SendfileTestServer', 'SMTPChannel', 'echo_client', 'st', 'ZipInfo', 
               'UserWarning', 'VerifyMode', 'NormalDist', 'date', 'SubPattern', 'Tokenizer', 'AsyncExitStack', 'Sigmasks', 'array', 'deque', 'Event', 'Vec2D', 'zipimporter', 
               'Profile', '_PlainTextDoc', 'Call', '_SocketWriter']
TypeLen = len (SuportTypes)

def DataProvider (type):
    if type == 'NoneType':
        TypeIndex = random.randint(0, TypeLen-1)
        if TypeIndex%2 == 0:
            return None
        else:
            return DataProvider (SuportTypes [TypeIndex])
    elif type == 'str':
        pass
    elif type == 'int':
        pass
    elif type == 'bool':
        pass
    elif type == 'bytes':
        pass
    elif type == 'list':
        pass
    elif type == 'memoryview':
        pass
    elif type == 'tuple':
        pass
    elif type == 'dict':
        pass
    elif type == 'float':
        pass
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
    else:
        pass


def Encode (DataList):
    pass



def DeEncode (ByteStream):
    pass