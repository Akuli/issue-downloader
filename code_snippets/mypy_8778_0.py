class Foo:
    @classmethod
    def baz(cls):
        return cls.__name__


class Bar(Foo):
    pass
