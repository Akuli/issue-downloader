import attr

@attr.s
class Bar:
    b = attr.ib()

    @classmethod
    def make(cls, one: int) -> 'Bar':
        return cls(one)


@attr.s
class Foo:
    a = attr.ib(converter=Bar.make)
