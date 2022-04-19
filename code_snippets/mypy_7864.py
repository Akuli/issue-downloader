from typing import Callable, Iterable, TypeVar

A = TypeVar("A")
B = TypeVar("B")

def identity(x: A) -> A:
    return x

# ok
def _map(queue: Iterable[B], function: Callable[[B], A]) -> Iterable[A]:
    return map(function, queue)

# fails
def _map2(queue: Iterable[B], function: Callable[[B], A] = identity) -> Iterable[A]:
    return map(function, queue)
