from typing import Callable, TypeVar
from typing_extensions import ParamSpec, Concatenate

P = ParamSpec("P")
T = TypeVar("T")


def identity(func: Callable[P, T]) -> Callable[P, T]:
    def _wrapped(*args: P.args, **kwargs: P.kwargs) -> T:
        return func(*args, **kwargs)

    return _wrapped


def int_identity(func: Callable[Concatenate[int, P], T]) -> Callable[Concatenate[int, P], T]:
    # identify should preserve the signature of _wrapped
    # error: Argument 1 to "identity" has incompatible type "Callable[[Arg(int, 'number'), **P], T]"; expected "Callable[[Arg(int, 'number'), **P], T]"
    @identity
    def _wrapped(number: int, *args: P.args, **kwargs: P.kwargs) -> T:
        return func(number, *args, **kwargs)

    return _wrapped
