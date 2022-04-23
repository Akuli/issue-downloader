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


if isinstance(foo_union, SupportsFunc):
    reveal_type(foo_union)  # N: Revealed type is '__main__.FooOverload'
else:
    reveal_type(foo_union)  # N: Revealed type is '__main__.Foo'



# NOTE: a `not isinstance` check also reveals a `Union`
if isinstance(foo_union, SupportsFunc):
    reveal_type(foo_union)  # N: Revealed type is '__main__.FooOverload'
else:
    reveal_type(foo_union)  # N: Revealed type is 'Union[__main__.FooOverload, __main__.Foo]'

