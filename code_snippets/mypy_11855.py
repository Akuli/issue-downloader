from typing import ParamSpec, Callable, TypeAlias

P = ParamSpec("P")

c: TypeAlias = Callable[P, int]

def f(n: c[P]) -> c[P]:
    ...
