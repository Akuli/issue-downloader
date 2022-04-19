import functools
from typing import Iterable, TypeVar, Callable

T1 = TypeVar('T1')
T2 = TypeVar('T2')

def chain(
        functions: Iterable[Callable[[T1], T1]]
    ) -> Callable[[T1], T1]:

    def compose(
            f: Callable[[T1], T1],
            g: Callable[[T1], T1]
        ) -> Callable[[T1], T1]:
        def h(x: T1) -> T1:
            return g(f(x))
        return h

    def identity(x: T1) -> T1:
        return x

    return functools.reduce(compose, functions, identity)

def add_one(x):
    return x + 1

def mul_two(x):
    return x * 2

assert chain([add_one, mul_two, mul_two, add_one])(7) == 33