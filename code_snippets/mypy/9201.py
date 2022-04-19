# makes_bug.py

from typing import Generic, Type, TypeVar

T = TypeVar('T')

class Foo(Generic[T]):
    def __init__(self, value: T) -> None: ...
    @classmethod
    def construct(cls) -> Foo[str]:
        return cls('bar')
