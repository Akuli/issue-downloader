from typing import Generic, Iterable, TypeVar

T = TypeVar('T')
S = TypeVar('S')

class Outer(Generic[T]):
    class Bad(Iterable[T]):       # Error
        ...
