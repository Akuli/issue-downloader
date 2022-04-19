from functools import partial
from typing import Callable, Generic, TypeVar

from typing_extensions import ParamSpec

R = TypeVar('R')
P = ParamSpec('P')

class custom_vjp(Generic[P, R]):
    def __init__(self, fun: Callable[P, R], x: int = 0):
        self.fun = fun

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        return self.fun(*args, **kwargs)

partial(custom_vjp, x=0)  # error: Argument 1 to "partial" has incompatible type "Type[custom_vjp[Any, Any]]"; expected "Callable[..., custom_vjp[P, R]]"  [arg-type]
