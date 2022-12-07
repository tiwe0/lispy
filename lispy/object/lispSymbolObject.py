from weakref import WeakValueDictionary
from lispy.object.lispObject import LispObject


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
        self.name = symbol_name
        self.slot_vari = slot_vari
        self.slot_func = slot_func
        self.interning()

    def eval_as_variable(self):
        if self.slot_vari:
            return self.slot_vari
        raise Exception("Symbol with void variable!")

    def eval_as_function(self):
        if self.slot_func:
            return self.slot_func
        raise Exception("Symbol with void function!")

    def interning(self):
        if not self.name in LispSymbolObject.symbol_bucket:
            LispSymbolObject.symbol_bucket[self.name] = self

    def interned(self):
        return self.name in LispSymbolObject.symbol_bucket

    def __del__(self):
        if self.interned():
            LispSymbolObject.symbol_bucket.pop(self.name)

from lispy.prime import *

