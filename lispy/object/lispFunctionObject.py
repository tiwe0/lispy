import typing
from lispy.object.lispObject import LispObject
from lispy.error import LispyWrongArgsNumException
from abc import abstractmethod
from typing import Callable
if typing.TYPE_CHECKING:
    from lispy.object.lispFormObject import LispFormObject, LispListObject

class LispFunctionObject(LispObject):
    def __init__(self, token):
        super().__init__(token=token)
        self.type = "FUNCTION"
        self.def_func: 'Callable' = lambda *x: x
        self.args_num: 'int' = -1

    def as_boolean(self):
        return True

    def check_args_num(self, context):
        if self.args_num == -1:
            return True
        if not (len(context)-1) == self.args_num:
            raise LispyWrongArgsNumException(self, context)
        return True

    @abstractmethod
    def eval(self, context: 'LispFormObject'):
        pass

class LispFunctionLispObject(LispFunctionObject):
    """lispy函数对象."""
    def __init__(self, token=''):
        super().__init__(token=token)
        self.args = []
        self.type = "LISP FUNCTION"
        self.docs = None
        self.body_forms = []

    def eval(self, context: 'LispFormObject'):
        if len(context[1:]) != len(self.args):
            raise LispyWrongArgsNumException(self, context)

        # bind
        for symbol, value_form in zip(self.args, context[1:]):
            symbol.push(value_form.eval())

        for body_form in self.body_forms:
            value = body_form.eval()

        # unbild
        for symbol in self.args:
            symbol.pop()

        return value

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
    def __init__(self, token):
        super().__init__(token)
        self.type = "SPECIAL FORM"

class LispBuiltinFunctionObject(LispFunctionPrimitiveObject):
    def __init__(self, token, def_func):
        super().__init__(token)
        self.def_func = def_func
        self.type = "BUILTIN"

