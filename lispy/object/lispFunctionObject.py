import typing
from lispy.object.lispObject import LispObject
from abc import abstractmethod
from typing import Callable
if typing.TYPE_CHECKING:
    from lispy.object.lispFormObject import LispFormObject

class LispFunctionObject(LispObject):
    def __init__(self, token):
        super().__init__(token=token)
        self.type = "FUNCTION"
        self.def_func: 'Callable' = lambda *x: x

    @abstractmethod
    def eval(self, context: 'LispFormObject'):
        pass

class LispFunctionLispObject(LispFunctionObject):
    """lispy函数对象."""
    def eval(self, context: 'LispFormObject'):
        args = [param.eval() for param in context[1:]]
        pass

class LispMacroObject(LispFunctionObject):
    pass

class LispFunctionPrimitiveObject(LispFunctionObject):
    """基础函数对象."""
    def __init__(self, token):
        super().__init__(token=token)
        self.type = "PRIMITIVE FUNCTION"

    def eval(self, context: 'LispFormObject'):
        """基础函数对象存储的函数定义是基于python的."""
        args = [param.eval() for param in context[1:]]
        return self.def_func(*args)

class LispSpecialFormObject(LispFunctionPrimitiveObject):
    def __init__(self, token, def_func):
        super().__init__(token)
        self.def_func = def_func
        self.type = "SPECIAL FORM"

class LispBuiltinFunctionObject(LispFunctionPrimitiveObject):
    def __init__(self, token, def_func):
        super().__init__(token)
        self.def_func = def_func
        self.type = "BUILTIN"

from lispy.object.builtin import *
