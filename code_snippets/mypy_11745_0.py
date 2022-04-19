# main.py


from __future__ import annotations
from typing import Generic, Protocol, TypeVar     


T = TypeVar("T")
U = TypeVar("U", bound=SupportsIAdd)


class SupportsIAdd(Protocol):
    def __iadd__(self: T, other: T) -> T: ...        


class AddingAccumulatorParam(Generic[U]):
    def addInPlace(self, value1: U, value2: U) -> U:
        value1 += value2  # Fails
        return value1
