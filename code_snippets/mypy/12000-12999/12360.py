from __future__ import annotations

from typing import Protocol

class P(Protocol):
    def f(self) -> int: ...

class C:
    def f(self) -> int:
        return 5

class D:
    def f(self) -> int:
        return 6

x: tuple[P, ...] = ()
reveal_type(x)

x = (C(), D())
reveal_type(x)

for thing in x:
    print(thing.f())
