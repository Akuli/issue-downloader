from typing import Union

class A:
    x: Union[int, float]

def foo(x: Union[int, float], y: A) -> None:
    reveal_type(x)
    reveal_type(y.x)
