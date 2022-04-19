from typing import *
class C(Protocol):
    T = TypeVar('T')
    def foo(self, t: T) -> T:
        ...

class D:
    def foo(self, t):
        return t

c: C = D()  # mypy crashes here
