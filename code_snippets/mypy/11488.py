from abc import ABC, abstractmethod
from typing import overload


class Foo(ABC):
    @overload # error: An overloaded function outside a stub file must have an implementation
    @abstractmethod
    def foo(self, value: int) -> int:
        ...

    @overload
    @abstractmethod
    def foo(self, value: str) -> str:
        ...

    # (this fake impl shouldnt be necessary, that's the impl class's responsibility)
    # @abstractmethod
    # def foo(self, value: str | int) -> str | int:
    #     ...


class Bar(Foo):
    @overload
    def foo(self, value: int) -> int:
        ...

    @overload
    def foo(self, value: str) -> str:
        ...

    def foo(self, value: str | int) -> str | int:
        return 1
