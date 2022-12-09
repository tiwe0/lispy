class LispyWrongArgsNumException(Exception):
    def __init__(self, lisp_obj, context):
        super().__init__()
        self.obj = lisp_obj
        self.context = context

    def __repr__(self):
        return f"{self.obj} got Wrong num of args! Expect {self.obj.args_num} args, but got {self.context}"
