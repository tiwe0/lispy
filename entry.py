#!/usr/bin/env python3

import sys
import pprint
from lispy.core.interpreter import Interpreter
from lispy.core.reader import Reader
from lispy.object.lispSymbolObject import LispSymbolObject as S

def lispy():

    interpreter = Interpreter()
    pprint.pprint(S.symbol_bucket)

    while True:
        try:
            _input = input("lispy> ")
            print(interpreter.interpret(_input))
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            print('\nbye~')
            sys.exit(0)
        except Exception as e:
            print(repr(e))

if __name__ == "__main__":
    lispy()
#    reader = Reader()
