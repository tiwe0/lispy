from lispy.object.lispImmutableObject import LispImmutableObject

class LispBooleanObject(LispImmutableObject):
    def __init__(self, token: 'str'):
        super().__init__(token)
        self.type = 'STRING'
