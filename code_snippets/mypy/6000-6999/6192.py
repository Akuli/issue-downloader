from typing import NamedTuple


class C(NamedTuple):
    a: int = 1


print(C.a * 2)
