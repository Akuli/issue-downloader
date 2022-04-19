from typing import Callable


def foo(fn: Callable[[int, str], None] | Callable[[int], None]) -> None:
    ...


foo(lambda value: reveal_type(value)) #revealed type is Any
