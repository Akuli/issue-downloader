from typing_extensions import ParamSpec
from typing import Callable, TypeVar

P = ParamSpec("P")
R = TypeVar("R")

def foo(func: Callable[P, R]) -> Callable[P, R]:
    def _inner(*args: P.args, **kwargs: P.kwargs) -> R:
        x = kwargs.pop("x")
        y = enumerate(args)
        return func(*args, **kwargs)
    return _inner
