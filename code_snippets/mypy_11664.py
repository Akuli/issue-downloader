from typing import Any, Generic, TypeVar
T = TypeVar("T")

class Foo(Generic[T]):
    def __init__(self, value: T):
        self.value = value

def identity(value: T) -> Foo[T]:
    if isinstance(value, str):
        return Foo(value)
    return Foo(value)
