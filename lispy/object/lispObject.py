from abc import abstractmethod

class LispObject:
    """Lisp 基础对象类，用于表示Lisp中所有对象
    必须实现 eval 方法."""
    def __init__(self, token: 'str' = '_form'):
        self._token = token
        self._type = None

    def __repr__(self):
        return f"{self._token}"

    @abstractmethod
    def eval(self):
        pass

    @classmethod
    def create_lisp_object(cls, token: 'str'):
        from lispy.object.lispSymbolObject import LispSymbolObject
        from lispy.object.lispIntegerObject import LispIntegerObject
        token = token.strip()
        if token.isdigit():
            return LispIntegerObject(token)
        if token in LispSymbolObject.symbol_bucket:
            return LispSymbolObject.symbol_bucket[token]
        return LispSymbolObject(token)
