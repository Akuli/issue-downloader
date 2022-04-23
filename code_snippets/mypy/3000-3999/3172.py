from typing import TypeVar, Generic

T = TypeVar('T')
class A(Generic[T]):

    def f(self) -> None:
        x: T

from typing import TypeVar, Generic

T = TypeVar('T')
class A(Generic[T]):
    @staticmethod
    def f() -> None:
        x: T  # Error we don't yet provide: Invalid type "__main__.T"

from typing import TypeVar, Generic

T = TypeVar('T')
class A(Generic[T]):
    @classmethod
    def f(cls) -> None:
        x: T  # Error we don't yet provide: Invalid type "__main__.T"
