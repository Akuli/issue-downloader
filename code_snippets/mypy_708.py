from typing import Callable

class A:
    f = None  # type: Callable[[int], int]

    def __init__(self, g: Callable[[int], int]) -> None:
        self.f = g

f = None  # type: Callable[[int], int]

def g(x: int) -> int: return 0

f = g

