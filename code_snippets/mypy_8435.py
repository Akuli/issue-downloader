from dataclasses import dataclass
from typing import Generic, TypeVar, Union


T_co = TypeVar("T_co", covariant=True)
@dataclass(frozen=True)
class Foo(Generic[T_co]):
    bar: T_co


def handle_foo_int(foo: Foo[int]) -> None:
    pass


def handle_foo(foo: Foo[Union[int, str]]) -> None:
    if isinstance(foo.bar, int):
        handle_foo_int(foo)
