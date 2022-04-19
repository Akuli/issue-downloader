from typing import TypeVar, Generic

T = TypeVar('T')
class A(Generic[T]):

    def f(self) -> None:
        x: T
