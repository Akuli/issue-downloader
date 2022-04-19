class C(object):
    def __new__(cls, foo=None):
        obj = object.__new__(cls)
        obj.foo = foo
        return obj

x = C(foo=12)
print(x.foo)
