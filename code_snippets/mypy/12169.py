from typing import TypeVar, Generic, ParamSpec, Protocol, Callable
from functools import partial

T = TypeVar("T", covariant=True)
P = ParamSpec("P")

class JittedFunction(Protocol, Generic[P, T]):
  def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T:
    ...

  def lower(self) -> int:
    ...

def jit(fun: Callable[P, T], *, x: int) -> JittedFunction[P, T]:
    pass

@partial(jit, x=2)  # error: Argument 1 to "partial" has incompatible type "Callable[[Callable[P, Any], NamedArg(int, 'x')], JittedFunction[P]]"; expected "Callable[..., JittedFunction[P]]"  [arg-type]
def f(y: int) -> int:
    return y
