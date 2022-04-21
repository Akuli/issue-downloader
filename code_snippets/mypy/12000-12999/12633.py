from dataclasses import dataclass
from typing import Any, Callable, Generic, TypeVar


T = TypeVar("T")

@dataclass
class Parent(Generic[T]):
    f: Callable[[T], Any]

@dataclass
class Child(Parent[T]): ...


class A: ...
def func(obj: A) -> bool: ...

reveal_type(Child[A](func).f)
