from typing import Optional, Union, TypeVar

MyUnion = Union[int, str]
T = TypeVar("T")


def not_none(x: Optional[T]) -> T:
    assert x is not None
    return x


# Works
def f(i: Optional[int]) -> int:
    return not_none(i)


# Doesn't work
def g(u: Optional[MyUnion]) -> MyUnion:
    return not_none(u)
