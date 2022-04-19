from typing import Callable, Union, overload

def f(fn: Callable[[Union[int, str]], Union[int, str]]) -> None: pass

@overload
def g(x: int) -> int: ...
@overload
def g(x: str) -> str: ...
def g(x): ...

f(g)   # Currently error
