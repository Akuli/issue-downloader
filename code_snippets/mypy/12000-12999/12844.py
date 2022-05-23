from typing import Callable, TypeVar

from typing_extensions import ParamSpec

P = ParamSpec('P')
R = TypeVar('R')


def wrapper(func: Callable[P, R]) -> Callable[P, R]:
    return func


wrapper(list)([1, 2, 3])  # "Too many arguments"
