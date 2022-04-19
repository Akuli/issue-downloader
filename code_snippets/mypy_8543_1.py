from typing import NamedTuple

class C(NamedTuple):
    x: int

    __hash__ = object.__hash__
