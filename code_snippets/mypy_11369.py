T = TypeVar("T")
R = TypeVar("R")
Decorator = Callable[[Callable[..., T]], Callable[..., R]]

from typing import *

T = TypeVar("T")
R = TypeVar("R")
Decorator = Callable[[Callable[..., T]], Callable[..., R]]

# def to_list() -> Decorator[T, List[T]]:
def to_list() -> Callable[[Callable[..., T]], Callable[..., List[T]]]:
    def decorator(func):
        def wrapped(*args, **kwargs):
            return [func(*args, **kwargs)]
        return wrapped
    return decorator
reveal_type(to_list)
reveal_type(to_list())

@to_list()
def foo() -> int:
    return 1

assert foo() == [1]
reveal_type(foo())


def to_list2() -> Decorator[T, List[T]]: ...
reveal_type(to_list2)
reveal_type(to_list2())

@to_list2()
def foo2() -> int:
    return 1
    
assert foo() == [1]
reveal_type(foo2())

