from lispy.object.lispObject import LispObject


class LispIntegerObject(LispObject):
    """Lisp中表示整数的类，求值结果为自身表示的整数."""
    def __init__(self, token: 'str'):
        super().__init__(token)
        self.value = int(token)

    def eval(self):
        return self.value
