from typing import Literal


def myfun(a: Literal["a", "b", "c"]) -> str:
    return a


s = "a"

myfun(s)


def myfun2(a: Literal[1, 2]) -> int:
    return a


b = 2
myfun2(b)

c = 1 if s == "a" else 2
myfun2(c)
