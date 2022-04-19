class meta (type):
    pass

class value (metaclass=meta):
    pass


class submeta (meta):
    @property
    def attr(cls) -> int:
        return 42

class subvalue (metaclass=submeta):
    @property
    def attr(self) -> int:
        return 21

o = subvalue()
a = o.attr
print(a)
a = subvalue.attr
print(a)
