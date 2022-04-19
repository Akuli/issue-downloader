from typing import TypeVar, Callable, Tuple

T = TypeVar('T')

def f(x: Callable[..., T]) -> T:
    return x()

x: Tuple[str, ...] = f(tuple)
