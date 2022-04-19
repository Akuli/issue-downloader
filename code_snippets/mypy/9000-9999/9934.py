import types

class Cls:
    def meth(self):
        pass

assert isinstance(Cls.meth, types.FunctionType)  # no problem

x: types.FunctionType = Cls.meth
