from typing import *
class C(Protocol):
    T = TypeVar('T')
    def __call__(self, t: T) -> T:
        ...

def f(t: int) -> int:
    return t

g: C = f  # mypy crashes here
