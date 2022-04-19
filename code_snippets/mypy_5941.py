class Foo:
    __slots__ = ['a']


instance = Foo()
instance.a = 10  # <-- False positive ("Foo" has no attribute "a")
instance.b = 20  # <-- True positive

class Bar:
    __slots__ = {'a': int}

instance2 = Bar()
instance2.a = 10
instance2.a = 'foo'  # <-- I would expect an error here

