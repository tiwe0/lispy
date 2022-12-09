import sys
from math import prod
from lispy.object.lispSymbolObject import LispSymbolObject as S
from lispy.object.lispFunctionObject import LispBuiltinFunctionObject
from lispy.object.lispNumberObject import LispIntegerObject, LispFloatObject
from lispy.object.lispFormObject import LispListObject

def builtin_num(func):
    def builtin_func(*x):
        result = func([v.value for v in x])
        if isinstance(result, int):
            return LispIntegerObject(token=str(result))
        return LispFloatObject(token=str(result))
    return builtin_func

def builtin_fset(symbol, definition):
    "TODO BUG"
    symbol.slot_func = definition
    return definition

print('register builtin function')
S.interning_functions_with_token([
    LispBuiltinFunctionObject(token='+', def_func=builtin_num(sum)),
    LispBuiltinFunctionObject(token='*', def_func=builtin_num(prod)),
    LispBuiltinFunctionObject(token='fset', def_func=builtin_fset),
    LispBuiltinFunctionObject(token='symbol-value', def_func=lambda s: s.slot_vari),
    LispBuiltinFunctionObject(token='symbol-function', def_func=lambda s: s.slot_func),
    LispBuiltinFunctionObject(token='car', def_func=lambda x: x[0]),
    LispBuiltinFunctionObject(token='cdr', def_func=lambda x: LispListObject.build_list(*x[1:])),
    LispBuiltinFunctionObject(token='list', def_func=LispListObject.build_list),
    LispBuiltinFunctionObject(token='funcall', def_func=lambda *x: x[0].eval(context=x)),
    LispBuiltinFunctionObject(token='quit', def_func=lambda: sys.exit(0)),
])
