from typing import TypeVar, Union

T = TypeVar("T", bound=Union[str, int])

def a(x: T) -> T:
    if isinstance(x, str):
        return x
    return x
