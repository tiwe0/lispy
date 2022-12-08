import sys
from math import prod
from lispy.object.lispSymbolObject import LispSymbolObject as S
from lispy.object.lispFunctionObject import LispBuiltinFunctionObject
from lispy.object.lispNumberObject import LispIntegerObject, LispFloatObject

def builtin_sum(*x):
    result = sum((v.value for v in x))
    if isinstance(result, int):
        return LispIntegerObject(token=str(result))
    else:
        return LispFloatObject(token=str(result))

print('register builtin function')
S.interning_functions_with_token([
    LispBuiltinFunctionObject(token='+', def_func=builtin_sum),
    LispBuiltinFunctionObject(token='*', def_func=lambda *x: prod(x)),
    ## and 和 or 本质不是函数，后面会改
    LispBuiltinFunctionObject(token='and', def_func=lambda *x: all(x)),
    LispBuiltinFunctionObject(token='or', def_func=lambda *x: any(x)),
    LispBuiltinFunctionObject(token='quit', def_func=lambda: sys.exit(0)),
])
