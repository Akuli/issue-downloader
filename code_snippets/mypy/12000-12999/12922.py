from typing import ParamSpec, TypeVar, Concatenate, Callable, overload

P = ParamSpec("P")
R = TypeVar("R")
S = TypeVar("S")

@overload
def bar(x: Callable[Concatenate[S, P], R]) -> str: ...
@overload
def bar(x: Callable[P, R]) -> int: ...
def bar(x: Callable[..., R]) -> str | int: ...
