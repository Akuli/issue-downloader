from typing import Callable, ParamSpec, TypeVar

T = TypeVar("T")

P = ParamSpec("P")
R = TypeVar("R")

def call(f: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> R:
    return f(*args, **kwargs)

def identity(x: T) -> T:
    return x

call(identity, 2)  # error: Argument 2 to "call" has incompatible type "int"; expected "T"

y: int = call(identity, 2)  # error: Incompatible types in assignment (expression has type "T", variable has type "int")
