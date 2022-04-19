from typing import Callable, Tuple, TypeVar, overload

T = TypeVar('T')
A0 = TypeVar('A0')
A1 = TypeVar('A1')


@overload
def foo(
    vars: Tuple[A0],
    op: Callable[[A0], T]
) -> T: ...


@overload
def foo(
    vars: Tuple[A0, A1],
    op: Callable[[A0, A1], T]
) -> T: ...


def foo(vars, op):
    pass


def foo_not_overloaded(
    vars: Tuple[A0, A1],
    op: Callable[[A0, A1], T]
) -> T:
    pass


a = 5
b = 3

foo((a, b), lambda a, b: a - b)
