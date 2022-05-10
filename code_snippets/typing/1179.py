from typing import TypeVar, Callable

T = TypeVar('T')

MkFoo = Callable[[T], list[T]]

def foo(mkfoo: MkFoo) -> None:
    _ = mkfoo(0)

def foo(mkfoo: Callable[[T], list[T]]) -> None:
    _ = mkfoo(0)
