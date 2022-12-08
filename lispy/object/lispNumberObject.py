from lispy.object.lispImmutableObject import LispImmutableObject

class LispNumberObject(LispImmutableObject):
    """lispy 中表示数字的类."""
    def __init__(self, token: 'str'):
        super().__init__(token)
        self.value = int(token)
        self.type = 'NUMBER'

    def __add__(self, other: 'LispNumberObject'):
        if isinstance(self, LispIntegerObject) and isinstance(other, LispIntegerObject):
            return LispIntegerObject(self.value+other.value)
        return LispFloatObject(self.value+other.value)

    def __mul__(self, other: 'LispNumberObject'):
        if isinstance(self, LispIntegerObject) and isinstance(other, LispIntegerObject):
            return LispIntegerObject(self.value*other.value)
        return LispFloatObject(self.value*other.value)

    def __div__(self, other: 'LispNumberObject'):
        if other.value == 0:
            raise ZeroDivisionError()
        return LispFloatObject(self.value/other.value)

class LispFloatObject(LispNumberObject):
    """lispy 中表示浮点数的类."""
    def __init__(self, token: 'str'):
        super().__init__(token)
        self.value = float(token)
        self.type = 'FLOAT'

class LispIntegerObject(LispNumberObject):
    """Lisp中表示整数的类，求值结果为自身表示的整数."""
    def __init__(self, token: 'str'):
        super().__init__(token)
        self.value = int(token)
        self.type = 'INTEGER'

