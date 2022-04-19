import typing

T = typing.TypeVar('T', str, int)


class Base(typing.Generic[T]):

    def __init__(self, bar: T):
        self.bar: T = bar


class Child(Base[T]):

    def __init__(self, bar: T):
        super().__init__(bar)
