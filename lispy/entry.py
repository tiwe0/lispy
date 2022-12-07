#!/usr/bin/env python3

import sys
from lispy.core.interpreter import Interpreter

def lispy():
    interpreter = Interpreter()

    while True:
        _input = input("lispy> ")
        try:
            print(interpreter.interpret(_input))
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            print('bye~')
            sys.exit(0)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    lispy()
