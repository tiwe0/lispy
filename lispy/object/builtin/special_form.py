from lispy.object.lispFunctionObject import LispSpecialFormObject, LispFunctionLispObject
from lispy.object.lispSymbolObject import LispSymbolObject
from lispy.object.lispBooleanObject import LispBooleanObject
from lispy.error import LispyWrongArgsNumException

S = LispSymbolObject

class LispSpecialFormObject_lambda(LispSpecialFormObject):
    def eval(self, context):
        args = context[1]
        docs = context[2]
        body_forms = context[3:]
        lambda_obj = LispFunctionLispObject()
        lambda_obj.type = "LAMBDA FUNCTION"
        lambda_obj.args, lambda_obj.docs, lambda_obj.body_forms = args, docs, body_forms
        return lambda_obj

class LispSpecialFormObject_setq(LispSpecialFormObject):
    def eval(self, context):
        if len(context[1:]) != 2:
            raise LispyWrongArgsNumException(self, context)
        assert isinstance(context[1], LispSymbolObject)
        value = context[2].eval()
        context[1].slot_vari = value
        return value

class LispSpecialFormObject_quote(LispSpecialFormObject):
    def eval(self, context):
        if len(context[1:]) != 1:
            raise LispyWrongArgsNumException(self, context)
        return context[1]

class LispSpecialFormObject_and(LispSpecialFormObject):
    def eval(self, context):
        for lisp_form_object in context[1:]:
            if not LispBooleanObject.to_boolean(lisp_form_object.eval()):
                return LispBooleanObject(False)
        return LispBooleanObject(True)

class LispSpecialFormObject_or(LispSpecialFormObject):
    def eval(self, context):
        for lisp_form_object in context[1:]:
            if LispBooleanObject.to_boolean(lisp_form_object.eval()):
                return LispBooleanObject(True)
        return LispBooleanObject(False)

class LispSpecialFormObject_cond(LispSpecialFormObject):
    pass

class LispSpecialFormObject_let(LispSpecialFormObject):
    """Special Form: let (bindings…) forms…"""
    def eval(self, context):
        if len(context) <= 2:
            raise LispyWrongArgsNumException(self, context)
        bindings = context[1]
        forms = context[2:]

        # eval value-forms
        value_forms = [bind_form[1].eval() for bind_form in bindings]

        # tmp bind
        symbols = [bind_form[0] for bind_form in bindings]
        for symbol, value_form in zip(symbols, value_forms):
            symbol.push(value_form)

        # eval forms
        for form in forms:
            value = form.eval()

        # tmp unbind
        for symbol in symbols:
            symbol.pop()

        return value

class LispSpecialFormObject_lets(LispSpecialFormObject):
    def eval(self, context):
        if len(context) <= 2:
            raise LispyWrongArgsNumException(self, context)
        bindings = context[1]
        forms = context[2:]

        # tmp bind
        for bind_form in bindings:
            symbol = bind_form[0]
            value_form = bind_form[1]
            symbol.push(value_form.eval())

        # eval forms
        for form in forms:
            value = form.eval()

        # tmp unbind
        for bind_form in bindings:
            symbol = bind_form[0]
            symbol.pop()

        return value

class LispSpecialFormObject_if(LispSpecialFormObject):
    def eval(self, context):
        if len(context[1:]) not in (2, 3):
            raise LispyWrongArgsNumException(self, context)
        condition = context[1]
        if condition.eval().as_boolean():
            return context[2].eval()
        if len(context[1:]) == 2:
            return LispBooleanObject(False)
        for lisp_form_object in context[3:]:
            value = lisp_form_object.eval()
        return value

class LispSpecialFormObject_while(LispSpecialFormObject):
    def eval(self, context):
        condition = context[1]
        forms = context[2:]
        while condition.eval().as_boolean():
            for form in forms:
                value = form.eval()
        return value

class LispSpecialFormObject_prog1(LispSpecialFormObject):
    def eval(self, context):
        if len(context) <= 2:
            raise LispyWrongArgsNumException(self, context)
        value = context[1].eval()
        for form in context[2:]:
            form.eval()
        return value

class LispSpecialFormObject_prog2(LispSpecialFormObject):
    def eval(self, context):
        if len(context) <= 3:
            raise LispyWrongArgsNumException(self, context)
        context[1].eval()
        value = context[2].eval()
        for form in context[2:]:
            form.eval()
        return value

class LispSpecialFormObject_progn(LispSpecialFormObject):
    def eval(self, context):
        if len(context) <= 1:
            raise LispyWrongArgsNumException(self, context)
        for form in context[1:]:
            value = form.eval()
        return value

print("interning special form.")
S.interning_functions_with_token([
    LispSpecialFormObject_setq(token='setq'),
    LispSpecialFormObject_quote(token='quote'),
    LispSpecialFormObject_lambda(token='lambda'),
    LispSpecialFormObject_and(token='and'),
    LispSpecialFormObject_or(token='or'),
    LispSpecialFormObject_cond(token='cond'),
    LispSpecialFormObject_if(token='if'),
    LispSpecialFormObject_while(token='while'),
    LispSpecialFormObject_prog1(token='prog1'),
    LispSpecialFormObject_prog2(token='prog2'),
    LispSpecialFormObject_progn(token='progn'),
    LispSpecialFormObject_let(token='let'),
    LispSpecialFormObject_lets(token='let*'),
])
