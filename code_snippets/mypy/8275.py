from typing import Callable, TypeVar, Generic

def foo() -> int:
    return 1

T = TypeVar('T')
bar: Callable[[], T] = foo
