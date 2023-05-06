import ssl
from ssl import *
def demoFunc(alpn_protocols):
    try:
        obj = ssl.SSLContext()
        obj.set_alpn_protocols(alpn_protocols)                           
    except (CertificateError,NotImplementedError,
            PermissionError,SSLError) as e:
        pass
demoFunc ("")

