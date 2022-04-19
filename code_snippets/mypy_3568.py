from typing import TypeVar, Generic, Callable

A = TypeVar('A')
B = TypeVar('B')
E = TypeVar('E', bound=BaseException)


class Child(Generic[A]):
    def __init__(self, x):
        # type: (E) -> None
        self.x = x

    def fun(self, s, f):
        # type: (Callable[[A], Child[B]], Callable[[E], Child[B]]) -> Child[B]
        return f(self.x)  # <----- error here
