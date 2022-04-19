from typing import Generic, TypeVar


T = TypeVar("T", int, float)


class Foo(Generic[T]):
    def __init__(self, val: T):
        self.data: T = val 


def bar(x: T) -> Foo[T]:
    return Foo(x)


x = bar(1)
x = bar(2.0) # error thrown by mypy
