from functools import partial
from typing import Any, Callable, Generic, Tuple, TypeVar

ReturnValue = TypeVar('ReturnValue')

class custom_vjp(Generic[ReturnValue]):
  def __init__(self,
               fun: Callable[..., ReturnValue],
               nondiff_argnums: Tuple[int, ...] = ()):
      self.fun = fun

  def __call__(self, *args: Any, **kwargs: Any) -> ReturnValue:
      return self.fun(*args, **kwargs)

  def defvjp(self,
             fwd: Callable[..., Tuple[ReturnValue, Any]]) -> None:
      pass

# @custom_vjp  (works with this)
@partial(custom_vjp, nondiff_argnums=(0,))
def f() -> None:
    pass

def fwd() -> tuple[None, None]:
    pass

f.defvjp(fwd)

f()
