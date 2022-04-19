from typing import TypeVar, Generic

T = TypeVar('T')

class Base(Generic[T]):
    def __init__(self, item: T) -> None:
        self.item = item
    def foo(self) -> None:
        pass

class Sub(Base[T]):
    def foo(self: Sub[str]) -> None:
        self.item + 'no'

# This is why the above is unsafe.
a: Base[int] = Sub(0)
a.foo()
