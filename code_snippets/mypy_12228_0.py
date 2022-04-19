from typing import overload, Protocol, runtime_checkable
from collections.abc import Sequence

class Foo:
    def func(self, a: int) -> float: ...

class FooOverload:
    @overload
    def func(self, a: int) -> float: ...
    @overload
    def func(self, a: str) -> Sequence[float]: ...

@runtime_checkable
class SupportsFunc(Protocol):
    @overload
    def func(self, a: int) -> float: ...
    @overload
    def func(self, a: str) -> Sequence[float]: ...

foo_union: FooOverload | Foo
