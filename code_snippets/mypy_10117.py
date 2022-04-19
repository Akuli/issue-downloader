# example.py

import inspect
from typing import Union, Callable, Type


def some_func(
        error: Union[Callable[..., BaseException], Type[BaseException]]
)->None:
    if (inspect.isfunction(error) or inspect.ismethod(error)):
        reveal_type(error)
    else:
        reveal_type(error)
