import itertools
from collections import deque
from lispy.object.lispObject import LispObject

class LispFormObject(LispObject):
    """抽象出Lisp表达式的类.

    求值时

    1. 将第一位作为符号，按函数求值获得函数

    2. 余下位有两种可能，若不为表达式，则将其作为符号，按变量求值获得变量值
    若为表达式，则重复上述逻辑求值

    3. 将余下求值结果作为参数传入第一位求值得到的函数进行运算，将运算结果作为
    该表达式的求值结果
    """
    def __init__(self, token = '_form'):
        super().__init__(token=token)
        self._slots = deque()

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop = key.start, key.stop
            if not stop:
                stop = len(self._slots)
            return list(itertools.islice(self._slots, start, stop))
        return self._slots[key]

    def push(self, sub_form: 'LispObject'):
        self._slots.append(sub_form)

    def push_left(self, sub_form: 'LispObject'):
        self._slots.appendleft(sub_form)

    def __repr__(self):
        return '(' + ' '.join((repr(t) for t in self._slots)) + ')'

    def eval(self):
        func = self[0].eval_as_function()
        args = [param.eval() for param in self[1:]]
        return func(*args)

LispLispObject = LispFormObject

