from typing import *
class C(Protocol):
    T = TypeVar('T')
    def __call__(self, t: T) -> T:
        ...

def f(t: int) -> int:
    return t

g: C = f  # mypy crashes here

from typing import *
class C(Protocol):
    T = TypeVar('T')
    def foo(self, t: T) -> T:
        ...

class D:
    def foo(self, t):
        return t

c: C = D()  # mypy crashes here
