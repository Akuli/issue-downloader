def outer(cls):
    class C(cls):  # E: Invalid type "cls"
        def meth(self):
            super(C, self).meth()  # E: "meth" undefined in superclass

cls = ...
class C(cls):  # E: Invalid type "cls"
    def meth(self):
        super(C, self).meth()  # E: "meth" undefined in superclass
