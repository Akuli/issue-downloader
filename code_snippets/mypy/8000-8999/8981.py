from typing import Any, Generic, TypeVar

T = TypeVar('T', bound=int)

class C(Generic[T]):
    x: T

c: C[Any] = C()
c.x = 123
c.x = 'abc'
