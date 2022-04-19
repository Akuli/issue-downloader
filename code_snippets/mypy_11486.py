from typing import TypeVar, Callable

T = TypeVar("T")

class A:
    def __init__(self, a: int) -> None:
        ...

def foo(t: type[T]) -> T:
    return t()

foo(A)  # SUS ALERT!
