from typing import TypeVar

T = TypeVar("T", int, str)


def foo(cls: type[T]) -> T:
    ...

asdf: type

reveal_type(type) # error: Expression type contains "Any"

a = foo(asdf) # no error

reveal_type(a) # int
