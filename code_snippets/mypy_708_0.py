from typing import Callable

class A:
    f = None  # type: Callable[[int], int]

    def __init__(self, g: Callable[[int], int]) -> None:
        self.f = g
