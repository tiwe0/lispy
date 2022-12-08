import typing
from lispy.object.lispObject import LispObject
if typing.TYPE_CHECKING:
    from lispy.object.lispFunctionObject import LispFunctionObject
    from typing import Optional


class LispSymbolObject(LispObject):
    """表示Lisp中Symbol的类，其求值结果取决于其位置

    LispSymbolObject 具有两个槽: `slot_vari` 和 `slot_func`

    作为变量时，求值结果为 `slot_vari` 的值

    作为函数时，求值结果为 `slot_func` 的函数定义
    """
    symbol_bucket = {}

    def __init__(self, symbol_name, slot_vari = None, slot_func = None):
        if symbol_name in LispSymbolObject.symbol_bucket:
            return
        super().__init__(symbol_name)
        self.type = 'SYMBOL'
        self.symbol_name = symbol_name
        self.slot_vari = slot_vari
        self.slot_func: 'Optional[LispMacroObject, LispFunctionObject, LispSymbolObject]' = slot_func
        self.interning()

    def eval(self):
        if self.slot_vari:
            return self.slot_vari
        raise Exception("Symbol with void variable!")

    def eval_as_variable(self):
        if self.slot_vari:
            return self.slot_vari
        raise Exception("Symbol with void variable!")

    def eval_as_function(self):
        return self.inderect()

    def inderect(self):
        if not self.slot_func:
            raise Exception("Symbol with void function!")
        if self.slot_func and isinstance(self.slot_func, LispSymbolObject):
            return self.slot_func.inderect()
        return self.slot_func

    def interning(self):
        if not self.symbol_name in LispSymbolObject.symbol_bucket:
            LispSymbolObject.symbol_bucket[self.symbol_name] = self

    def interned(self):
        return self.symbol_name in LispSymbolObject.symbol_bucket

    def __del__(self):
        if self.interned():
            LispSymbolObject.symbol_bucket.pop(self.symbol_name)

    @classmethod
    def interning_object_with_token(cls, lisp_object: 'LispObject'):
        token = lisp_object.token
        symbol = LispSymbolObject(symbol_name=token)
        symbol.slot_vari = lisp_object
        return symbol

    @classmethod
    def interning_function_with_token(cls, lisp_function_object: 'LispFunctionObject'):
        token = lisp_function_object.token
        symbol = LispSymbolObject(symbol_name=token)
        symbol.slot_func = lisp_function_object
        return symbol

    @classmethod
    def interning_functions_with_token(cls, lisp_function_objects: 'list[LispFunctionObject]'):
        for lisp_function_object in lisp_function_objects:
            cls.interning_function_with_token(lisp_function_object)
