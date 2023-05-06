
from email.policy import *
import email
import email.policy
import re
from email._policybase import Policy


def demoFunc(name, value):
    try:
        obj = email.policy.EmailPolicy()
        ret = obj.header_fetch_parse(name, value)

    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError) as e:
        pass

demoFunc("To", "laLc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5Lc7A%15?xpw#7@do$Ff4ZhgSEx5NnL*T)QNr3HR8NqB5vb>)QNr3HR8NqB5vbu^s#^0f4Zhpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5Lc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb)QNr3HR8NqB5vbgSEx5NnLc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5Lc7A%pw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5Lc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb)QNr3HR8NqB5vbgSEx5NnLc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5Lc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb)Q?Nr3HR8NqB5vbu^s#^0f4Zhx5NnLc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5Lc7A%pw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5Lc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb)QNr3HR8NqB5vbgSEx5NnLc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5Lc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb)Q?Nr3HR8NqB5vbu^s#^0f4Zh)QNr3HR8NqB5vbgSEx5NnLT)QNr3HR8NqB5vbNr3HR8NT)QNr3HR8NqB5v15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((:)Q)QNr3HR8NqB5v)Q?Nr3HR8NqB5vbu^s#^0f4Zh)QNr3HR8NqB5vbgSEx5NnLT)QNr3HR8NqB5vbNr3HR8NT)QNr3HR8NqB5v15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((:)Q)QNr3HR8NqB5v)QNr3HR8NqB5vbgSEx5NnLT)QNr3HR8NqB5vbNr3HR8NT)QNr3HR8NqB5v15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((:)Q)QNr3HR8NqB5vbu^s#^0f4Zhpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5Lc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb0)QNr3HR8NqB5vbgSEx5Nn)QNr3HR8NqB5vbgSEx5NnLT)QNr3HR8NqB5vbNr3HR8NT)QNr3HR8NqB5v15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((:)Q)QNr3HR8NqB5vbu^s#^0f4Zhpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5Lc7A%15?xpw#7@do$Ff4ZhgSEx5NnLT)QNr3HR8NqB5vb0)QNr3HR8NqB5vbgSEx5NnLT)QNr3HR8NqB5vbNr3HR8NT)QNr3HR8NqB5vbNr3HR8N32")

