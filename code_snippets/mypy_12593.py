from functools import partial
from typing import TypeVar, Callable
from typing_extensions import ParamSpec, Protocol

T = TypeVar('T', covariant=True)
P = ParamSpec('P')

class Wrapped(Protocol[P, T]):
  def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
    pass

def jit(f: Callable[P, T]) -> Wrapped[P, T]:
    return f

def f(x: int, y: int):
    return x + y

partial_jit = partial(jit)
partial_jit(f)(0, 0)

from functools import partial
from typing import TypeVar, Callable
from typing_extensions import ParamSpec

T = TypeVar('T', covariant=True)
P = ParamSpec('P')

def jit(f: Callable[P, T]) -> Callable[P, T]:
    return f

def f(x: int, y: int):
    return x + y

partial_jit = partial(jit)
partial_jit(f)(0, 0)

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

