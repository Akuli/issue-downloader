from typing import Callable, TypeVar

A = TypeVar("A")
B = TypeVar("B")


def func(a: A, b: B, fn: Callable[[A], A]) -> A | B:
    ...


inferred = func(
    1,
    None,
    lambda value: reveal_type(value),  # Revealed type is "builtins.int"
)
reveal_type(inferred)  # "Union[builtins.int, None]"

explicit: int | None
explicit = func(
    1,
    None,
    lambda value: reveal_type(value), # Revealed type is "Union[builtins.int, None]"
)
reveal_type(explicit)  # "Union[builtins.int, None]"
