from lispy.object.lispObject import LispObject
from lispy.object.lispFormObject import LispFormObject


class Reader:
    """读取器，将文本代码转换为Lisp对象."""
    _instance = None
    prime_funcs = {""}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def _pre_process(self, form_str: 'str'):
        std_form_str = form_str.replace('\n', '').replace('\t', ' ').strip()
        std_form_str = std_form_str.replace('(', ' ( ').replace(')', ' ) ')
        std_form_str = ' '.join(std_form_str.split())
        return std_form_str

    def _assert_pairs_valid(self, std_form_lst: 'List[str]'):
        pairs_stack = []
        for token in std_form_lst:
            if token == '(':
                pairs_stack.append('(')
            elif token == ')':
                pairs_stack.pop()
        if len(pairs_stack) != 0:
            return False
        return True

    def _convert_into_lispObject(self, std_form_lst: 'List[str]'):
        assert self._assert_pairs_valid(std_form_lst), 'Invalid pairs match!'
        token_stack = []

        def consume():
            lisp_form_object = LispFormObject()
            while token_stack:
                token = token_stack.pop()
                if token == ')':
                    continue
                if token == '(':
                    break
                if not isinstance(token, LispObject):
                    token = self.read_a_token(token)
                lisp_form_object.push_left(token)
            return lisp_form_object

        while not (len(token_stack) == 1
                   and isinstance(token_stack[0], LispObject)):
            token = std_form_lst.pop(0)
            token_stack.append(token)
            if token == ')':
                token_stack.append(consume())

        return token_stack[-1]

    def read_a_form(self, form_str: 'str'):
        std_form_lst = self._pre_process(form_str).split()
        std_form = self._convert_into_lispObject(std_form_lst)
        assert isinstance(std_form, LispObject)
        return std_form

    def read_a_token(self, token_str: 'str'):
        token_str = token_str.strip()
        lisp_object = LispObject.create_lisp_object(token_str)
        return lisp_object
