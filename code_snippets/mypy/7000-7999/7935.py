from typing import TypeVar, Generic, overload

T = TypeVar('T')

class C(Generic[T]):
    @overload
    def __new__(cls) -> C[None]: ...
    @overload
    def __new__(cls, item: T) -> C[T]: ...
    def __new__(cls, item=None):
        ...
    @classmethod
    def f(cls, x: T) -> T:
        return x

C.f(42)  # Argument 1 to "f" of "C" has incompatible type "int"; expected "None"
