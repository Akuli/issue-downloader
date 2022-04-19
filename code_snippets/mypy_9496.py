from typing import Callable, TypeVar

Fn = TypeVar("Fn", bound=Callable[..., object])

def foo(fn: Fn) -> Fn:  # type safe usage
    fn(1)  # not type safe usage
