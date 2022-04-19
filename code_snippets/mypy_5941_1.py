class Bar:
    __slots__ = {'a': int}

instance2 = Bar()
instance2.a = 10
instance2.a = 'foo'  # <-- I would expect an error here
