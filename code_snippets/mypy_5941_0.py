class Foo:
    __slots__ = ['a']


instance = Foo()
instance.a = 10  # <-- False positive ("Foo" has no attribute "a")
instance.b = 20  # <-- True positive
