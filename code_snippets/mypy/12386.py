from typing_extensions import ParamSpec
from typing import Callable

P = ParamSpec("P")

def foo(func: Callable[P, None]):
    def _inner(*args: P.args, **kwargs: P.kwargs):
        x = kwargs.pop("x")
