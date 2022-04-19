from typing import Type

from external import ExtBase


class Base(ExtBase):
    pass


class Concrete1(Base):
    pass


class Concrete2(Concrete1):
    pass


def f(x: Type[Base]) -> None:
    pass


def g(x: bool) -> None:
    #reveal_type(Base)
    #reveal_type(Concrete1)
    #reveal_type(Concrete2)
    #reveal_type(Concrete1 if x else Concrete2)
    f(Concrete1 if x else Concrete2)
