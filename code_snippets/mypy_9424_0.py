from typing import Optional, TypeVar

U = TypeVar('U', bound=Optional[int])


def f(u: U) -> U:
    if u is None:
        return None
    assert isinstance(u, int)  # removing this line causes it to pass.
    return u
