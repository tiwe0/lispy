from lispy.object.lispObject import LispObject

class LispImmutableObject(LispObject):
    """lispy 中表示不可变对象的类."""
    def __init__(self, token: 'str'):
        super().__init__(token)
        self.value = token
        self.type = 'IMMUTABLE'

    def eval(self):
        return self
