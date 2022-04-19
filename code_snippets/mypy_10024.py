from typing import *

class D(TypedDict): ...

class P(Protocol): ...

T = TypeVar('T', bound=P)

def foo(cls: Type[T]) -> T: ...

d:D = foo(D)
