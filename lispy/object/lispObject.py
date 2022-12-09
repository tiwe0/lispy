from abc import abstractmethod

class LispObject:
    """Lisp 基础对象类，用于表示Lisp中所有对象
    必须实现 eval 方法."""
    def __init__(self, token: 'str' = '_form'):
        self.token = token
        self.type = 'BASE'

    def __repr__(self):
        return f"{self.type}: {self.token}"

    @abstractmethod
    def as_boolean(self):
        raise NotImplementedError()

    @abstractmethod
    def eval(self):
        raise NotImplementedError()
