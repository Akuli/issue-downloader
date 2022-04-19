from typing import Callable, Union

def some_func(obj: Union[Callable, int]):
    if isinstance(obj, Callable):
        reveal_type(obj) # Type of "obj" is "(*args: Unknown, **kwargs: Unknown) -> Unknown | int"
    else:
        reveal_type(obj) # Type of "obj" is "(*args: Unknown, **kwargs: Unknown) -> Unknown | int"
