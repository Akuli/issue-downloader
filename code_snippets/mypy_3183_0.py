from typing import *

T = TypeVar('T', bound='A')

class X: ...

class Y(X): ...

class A(Iterable[X]):
    def __iter__(self) -> Iterator[X]: ...

class B(A, Iterable[Y]):
    def __iter__(self) -> Iterator[Y]: ...

b = B()
for x in b:
    reveal_type(x)  # 'Y*'

y = list(b)
reveal_type(y)  # 'builtins.list[X*]'
