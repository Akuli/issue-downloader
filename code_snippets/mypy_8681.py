from typing import Type, TypeVar, Tuple

T = TypeVar('T')


def func(a: T, a_type: Type[T]) -> Tuple[T, Type[T]]:
    return a, a_type


a1, a1_type = func(1, int)
a2, a2_type = func(1, str)

reveal_type(a1)
reveal_type(a1_type)
reveal_type(a2)
reveal_type(a2_type)
