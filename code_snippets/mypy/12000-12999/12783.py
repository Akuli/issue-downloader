from typing import Iterable

class X(Iterable[str]): ...

a: Iterable[str]
x: X
b: bool

if b:
    a = x or []
else:
    a = [""]
reveal_type(a)  # Revealed type is "Any"  TypeOfAny.special_form

a = x or [] if b else [""]
reveal_type(a)  # Revealed type is "list[str] | test.X | list[<nothing>]"

from typing import Iterable, NoReturn

class X(Iterable[str]): ...

a1: X | list[NoReturn]
a2: list[str]

b: bool

c: Iterable[str]
if b:
    c = a1
else:
    c = a2
reveal_type(c)  # Any
