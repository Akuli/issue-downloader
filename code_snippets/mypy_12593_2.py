from functools import partial
from typing import TypeVar, Callable
from typing_extensions import ParamSpec

T = TypeVar('T')
P = ParamSpec('P')


def jit(f: Callable[P, T]) -> Callable[P, T]:
    return f

def f(x: int, y: int):
    return x + y

partial_jit = partial(jit)
partial_jit(f)(0, 0)
