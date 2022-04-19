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

# main.py

from __future__ import annotations
from typing import Generic, Protocol, TypeVar     


T = TypeVar("T")
U = TypeVar("U", bound=SupportsIAdd)


class SupportsIAdd(Protocol):
    def __add__(self: T, other: T) -> T: ... 


class AddingAccumulatorParam(Generic[U]):
    def addInPlace(self, value1: U, value2: U) -> U:
        value1 += value2  # Passes just fine
        return value1

# main.py

from __future__ import annotations
from typing import Any, TypeVar              


class SupportsIAdd:          
    def __iadd__(self, other: Any) -> SupportsIAdd: ...         


class AddingAccumulatorParam:            
    def addInPlace(self, value1: SupportsIAdd, value2: SupportsIAdd) -> SupportsIAdd:            
        value1 += value2
        return value1

class AddingAccumulatorParam(Generic[U]):
    def addInPlace(self, value1: U, value2: U) -> U:
        return reveal_type(value1.__iadd__(value2))
