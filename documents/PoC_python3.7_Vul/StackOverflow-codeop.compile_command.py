
from codeop import *
import codeop

class demoCls():

    def __init__(self):
        pass

    def demoFunc(self, source, filename, symbol):
        try:
            ret = codeop.compile_command(source, filename, symbol)
        except (AssertionError, AttributeError, LookupError, OSError, SyntaxError, TypeError, ValueError) as e:
            pass


source = "LLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLC@v(3@LLLLLLLLLLLL(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuuuAuuuuuuuuuLLLLLLLLLx(u^uuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuu%LLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLC@v(3@LLLLLLLLLLLL(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu8LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLC@v(3@LLLLLLLLLLLL(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuuuAuuuuuuuuuLLLLLLLLLx(u^uuuuuuu[uuuuuuuuuAuuuuuuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLC@v(3@LLLLLLLLLLLL(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuuuAuuuuuuuuuLLLLLLLLLx(u^uuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuu%LLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLC@v(3@LLLLLLLLLLLL(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu8LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLC@v(3@LLLLLLLLLLLL(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuuuAuuuuuuuuuLLLLLLLLLx(u^uuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuu%LLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLC@v(3@LLLLLLLLLLLL(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuLLLLLLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuuuAuuuuuuuuuLLLLLLLLLx(u^uuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuuAuAuuuuuuLuuuuuuuuu[uuuuuuuu%LLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLC@v(3@LLLLLLLLLLLL(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuu7LLLLLLLLLLLLLLLLLLLLLLLLLLLLLuuuuzuuuuuuuuuuuu%uuuuuALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuLLLLLLx(2@LLLLLLLLLLLLLLLLLLLLLx(uuuuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuuuAuuuuuuuuuLLLLLLLLLx(u^uuuuuuu[uuuuuuuuuAuuuuuuLuuuuuuuuu[uuuuuuuuuAuuuuuuuuuuu%uuuuuAuAuuuuuuuuuuu%uuuuuAuuuuuuuuuuu%%%%"
filename = "x"
symbol = "exec"


dc = demoCls()
dc.demoFunc(source, filename, symbol)
