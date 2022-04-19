from typing import Type

class A:
    def __init__(self, x: int) -> None: pass

def f(t: Type[object]) -> None:
    t()  # ok, since `object()` is valid

f(A)  # no error reported!

class A:
    ...
    @classmethod
    def f(cls: Type[[int], A]) -> A:
        return cls(1)  # ok
