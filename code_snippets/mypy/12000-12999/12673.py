from __future__ import annotations
from typing import Callable

def decorate(c: classmethod[None]) -> Callable[[X], None]:
    def g(x: X) -> None:
        return c.__func__(type(x))
    return g

class X:
    @decorate  # error: Argument 1 to "decorate" has incompatible type "Callable[[Type[X]], None]"; expected "classmethod[None]"
    @classmethod
    def f(cls) -> None:
        print("okay")

x = X()
x.f()  # error: Invalid self argument "Type[X]" to class attribute function "f" with type "Callable[[X], None]"
