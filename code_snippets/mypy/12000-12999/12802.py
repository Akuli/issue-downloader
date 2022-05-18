def f(x: Optional[X]) -> None:
    if isinstance(x, Y):
        print(x.bar())

from typing import Optional, Protocol, runtime_checkable
from typing_extensions import reveal_type


class X:
    def foo(self) -> int:
        ...


@runtime_checkable
class Y(Protocol):
    def bar(self) -> int:
        ...


class Z(X):
    def foo(self) -> int:
        return 5

    def bar(self) -> int:
        return 6


def f(x: Optional[X]) -> None:
    reveal_type(x)
    if isinstance(x, Y):
        reveal_type(x)
        print(x.bar())


def g(x: X) -> None:
    reveal_type(x)
    if isinstance(x, Y):
        reveal_type(x)
        print(x.bar())


f(Z())
g(Z())
