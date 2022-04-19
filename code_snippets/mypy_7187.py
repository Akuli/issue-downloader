from typing import Callable, Union, Tuple

def f(x: Union[Callable[..., int], Callable[..., str]]) -> None: ...
x: Callable[..., Union[int, str]]
f(x)

def g(y: Union[Tuple[int], Tuple[str]]) -> None: ...
y: Tuple[Union[int, str]]
g(y)
