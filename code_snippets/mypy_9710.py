from typing import Tuple

def x(x: int, y: int) -> None:
    print(x, y)

def foo1(t: tuple) -> None:
    x(*t[:1], 1)

def foo2(t: tuple) -> None:
    x(*t[:2])

def foo3(t: Tuple[int]) -> None:
    x(*t[:1], 1)
