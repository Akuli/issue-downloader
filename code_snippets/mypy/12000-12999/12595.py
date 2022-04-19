from typing import TypeVar, Callable
from typing_extensions import Concatenate, ParamSpec, Protocol

T_co = TypeVar('T_co', covariant=True)
T = TypeVar('T')
P = ParamSpec('P')

class Wrapped(Protocol[P, T_co]):
  def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T_co:
    pass

def jit(f: Callable[P, T], *, a: bool) -> Wrapped[P, T]:
    return f

_T = TypeVar('_T')
_P = ParamSpec('_P')

def _make_factory(
    transform: Callable[Concatenate[Callable[P, T], _P], _T]
) -> Callable[_P, Callable[[Callable[P, T]], _T]]:
    return lambda *args, **kwargs: lambda f: transform(f, *args, **kwargs)

_make_jit = _make_factory(jit)
@_make_jit(a=True) # line 24
def f(x: int, y: int):
    return x + y

f(0, 0) # line 28
