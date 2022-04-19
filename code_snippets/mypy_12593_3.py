from functools import partial
from typing import TypeVar

F = TypeVar('F')

def jit(f: F) -> F:
    return f

def f(x: int, y: int):
    return x + y

partial_jit = partial(jit)
partial_jit(f)(0, 0) # error here
jit(f)(0, 0) # no error here
