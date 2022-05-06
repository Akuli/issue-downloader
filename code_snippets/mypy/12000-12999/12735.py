from typing import Callable, Concatenate, ParamSpec
from mypy_extensions import DefaultArg

P = ParamSpec("P")

def foo(f: Callable[P, None]) -> Callable[Concatenate[DefaultArg(int), P], None]:
    def g(n: int = 0, /, *args: P.args, **kwargs: P.kwargs) -> None:
        f(*args, **kwargs)

    return g
