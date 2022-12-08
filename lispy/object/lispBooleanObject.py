from lispy.object.lispImmutableObject import LispImmutableObject
from lispy.object.lispSymbolObject import LispSymbolObject as S

class LispBooleanObject(LispImmutableObject):
    def __init__(self, value: 'bool'):
        if value:
            token = 't'
        else:
            token = 'nil'
        super().__init__(token)
        self.value = value
        self.type = 'BOOLEAN'

    def __add__(self, other: 'LispBooleanObject'):
        return LispBooleanObject(self.value and other.value)

    def __or__(self, other: 'LispBooleanObject'):
        return LispBooleanObject(self.value or other.value)


print("interning bool symbol")
S.interning_object_with_token(LispBooleanObject(value=True))
S.interning_object_with_token(LispBooleanObject(value=False))
