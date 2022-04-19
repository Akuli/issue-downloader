from typing import Callable, TypeVar

T = TypeVar('T')
F = TypeVar('F', bound=Callable[..., int])

def call(func: Callable[..., T], *args: object) -> T:
    return func(*args)  # ok

def call2(func: Callable[..., int], *args: object) -> int:
    return call(func, *args)  # ok

def call3(func: F, *args: object) -> int:
    return call2(func, *args)  # ok

def call4(func: F, *args: object) -> int:
    return call(func, *args)  # error??
