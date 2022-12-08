from lispy.core.reader import Reader
from lispy.core.evaluator import Evaluator

class Interpreter:

    _instance = None
    _reader = Reader()
    _evaluator = Evaluator()

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def interpret(self, code: str):
        lisp_obj = self._reader.read_a_form(code)
        print(lisp_obj)
        value = self._evaluator.eval(lisp_obj)
        return value
