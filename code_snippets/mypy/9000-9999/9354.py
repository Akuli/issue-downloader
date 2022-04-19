from typing import Sequence
import attr

@attr.s
class A:
    a: Sequence[str] = attr.ib(converter=list)
A(["a"])
