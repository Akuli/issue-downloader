from typing import TypeVar

Num = TypeVar("Num", bound=int | float)


def add(a: Num, b: Num) -> Num:
    return a + b
