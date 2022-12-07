import sys
from math import prod
from lispy.object.lispSymbolObject import LispSymbolObject

LispSymbolObject(symbol_name='+', slot_func=lambda *x: sum(x))
LispSymbolObject(symbol_name='*', slot_func=lambda *x: prod(x))
LispSymbolObject(symbol_name='quit', slot_func=lambda: sys.exit(0))
