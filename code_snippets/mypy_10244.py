from dataclasses import dataclass
from typing import Generic, TypeVar, Callable

T = TypeVar('T')
R = TypeVar('R')
X = TypeVar('X')

@dataclass
class Box(Generic[T]):
    inner: T

@dataclass
class Cont(Generic[R]):
    run: Box[Callable[[X], R]]

def f(c: Cont[R]) -> R:
    return c.run.inner(3)

def const_two(x: T) -> str:
    return "two"

c = Cont(Box(const_two))
