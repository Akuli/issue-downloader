from typing import Callable, Generic, TypeVar

T_co = TypeVar("T_co", covariant=True)


class Foo(Generic[T_co]):
    def __init__(self, bar: Callable[[T_co], None]) -> None:
        self.bar = bar

    def good(self) -> "Foo[T_co]":
        return Foo(self.bar)

    def bad(self) -> "Foo[T_co]":  # error here
        return Foo(lambda x: None)  # not here

    def more_obvious_bad(self) -> "Foo[T_co]":
        fn: Callable[[T_co], None] = lambda x: None  # error here
        return Foo(fn)
