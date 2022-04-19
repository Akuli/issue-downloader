from typing import Callable

def my_function(callback: Callable[...]) -> None:
    callback()

from typing import Callable

def my_function(callback: Callable) -> None:
    callback()

