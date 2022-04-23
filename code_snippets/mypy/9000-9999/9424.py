from typing import Optional, TypeVar

U = TypeVar('U', bound=Optional[int])


def f(u: U) -> U:
    if u is None:
        return None
    assert isinstance(u, int)  # removing this line causes it to pass.
    return u

from typing import Optional, TypeVar, overload


@overload
def f(u: None) -> None: ...

@overload
def f(u: int) -> int: ...

def f(u: Optional[int]) -> Optional[int]:
    if u is None:
        return None
    assert isinstance(u, int)
    return u

class C: pass
class B(C): pass
class A(B): pass

T = TypeVar('T', bound=C)
def factory(cls: Type[T]) -> T:
    return cls()
