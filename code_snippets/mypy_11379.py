from typing import TypeVar, Union, Generic

T1 = TypeVar("T1", int, str, covariant=True)
T2 = TypeVar("T2", int, str)

class X1(Generic[T1]):
    def f(self) -> T1: ...
class X2(Generic[T2]):
    def f(self) -> T2: ...

def f1(x: X1[int]) -> None: ...
def f2(x: X2[int]) -> None: ...

f1(X1[int]())
f1(X1[bool]())

f2(X2[int]())
f2(X2[bool]())
