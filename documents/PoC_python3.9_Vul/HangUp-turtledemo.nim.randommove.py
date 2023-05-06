from turtledemo.nim import *
import turtledemo
import random
import turtle
import turtledemo.nim

def demoFunc(arg):
    try:
        turtledemo.nim.randommove(arg)
    except (AssertionError, AttributeError, LookupError, OSError, TypeError, ValueError, turtle.Terminator, turtle.TurtleGraphicsError) as e:
        pass


state = b"\x00\x00\x00\x00\x00\x00\x00\x01b\'((z(*yE)0P&OF4VSQVkevJ$OBH8sizeImDGe2oVs(q#EN*yleFkw!ffQIER%7#vw!VZGzV$7lS#J94Oyws,%HQP8WQF99T3WrKq!\'"
demoFunc(state)
