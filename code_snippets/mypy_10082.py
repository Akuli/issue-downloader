from typing import TypeVar
from typing_extensions import Protocol

T_co = TypeVar('T_co', covariant=True)

class C(Protocol[T_co]):
    def __call__(self) -> T_co: ...

def f(c: C) -> str:
    return c()

def g() -> bool:
    return True

f(g)

