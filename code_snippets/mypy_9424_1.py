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
