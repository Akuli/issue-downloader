from typing import TypeVar, Generic

T = TypeVar('T')
class A(Generic[T]):
    @classmethod
    def f(cls) -> None:
        x: T  # Error we don't yet provide: Invalid type "__main__.T"
