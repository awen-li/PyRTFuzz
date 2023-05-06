from email.policy import *
import email
import email.policy
import re
from email._policybase import Policy


class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, arg1,arg2):
        try:
            obj = email.policy.EmailPolicy()
            obj.header_store_parse(arg1,arg2)
            repr(obj)
        except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
            pass

name = "to"
value = "t%&$o%tp_orkersuse_counters PjhssTeΣkkr%XS((((((unters PjhssTeΣkkr%XS((((((((((((((((((((((((((((((((((((((((((( (((((((((((((((orkersuse_counters PjhssTeΣkkr%XS(((((((fork(((((((((((((((((((((((((((((((( ((((((((((((((((((jn((((((((((((((((((((((((((((((((((((( (((((((((((((((orkersuse_counters PjhssTeΣkkr%XS(((((((fork(((((((((((((((((((((((((((((((( ((((((((((((((((((jnPjnP(((jnPjnPQkXS"
dc = demoCls()
dc.demoFunc(name,value)

