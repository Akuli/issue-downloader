# foobar.py
from typing import NamedTuple, overload


A = NamedTuple("A", (("f", int),))
B = NamedTuple("B", (("q", int),))


@overload
def plain(a: A) -> int:
    ...

@overload
def plain(a: B) -> str:
    ...

def plain(a):
    if isinstance(a, A):
        return 4
    elif isinstance(a, B):
        return "4"
    else:
        raise TypeError()
