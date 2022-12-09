from lispy.object.lispObject import LispObject

class Evaluator:
    """求值器，对Lisp对象或Lisp表达式对象求值."""
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def _assert_lispObject(self, lisp_object: 'LispObject'):
        assert isinstance(lisp_object, LispObject), 'lisp_object should be LispObject instance'
        return True

    def eval(self, lisp_object: 'LispObject'):
        self._assert_lispObject(lisp_object)
        return lisp_object.eval()

    def _eval_as_function(self, lisp_object: 'LispObject'):
        self._assert_lispObject(lisp_object)
        if not hasattr(lisp_object, 'slot_function'):
            raise Exception("function void!")
        return lisp_object.slot_function

    def _eval_as_variable(self, lisp_object: 'LispObject'):
        self._assert_lispObject(lisp_object)
        if not hasattr(lisp_object, 'slot_variable'):
            raise Exception("variable void!")
        return lisp_object.slot_variable
