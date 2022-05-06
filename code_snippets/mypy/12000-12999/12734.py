from typing import Callable, Concatenate, ParamSpec

P = ParamSpec("P")
Q = ParamSpec("Q")

def foo(f: Callable[P, int]) -> Callable[P, int]:
    return f

def bar(f: Callable[Concatenate[str, bool, Q], int]) -> Callable[Concatenate[str, bool, Q], int]:
    return foo(f)
