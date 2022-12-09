from lispy.object.lispImmutableObject import LispImmutableObject
from lispy.object.lispSymbolObject import LispSymbolObject as S
import typing
if typing.TYPE_CHECKING:
    from lisipy.object.LispObject import LispObject

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

    def as_boolean(self):
        return self.value

    @classmethod
    def to_boolean(cls, lisp_object: 'LispObject'):
        # TODO
        return LispBooleanObject(lisp_object.as_boolean())

print("interning bool symbol")
S.interning_object_with_token(LispBooleanObject(value=True))
S.interning_object_with_token(LispBooleanObject(value=False))
