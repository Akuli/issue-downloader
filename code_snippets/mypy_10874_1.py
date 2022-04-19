from typing import *
from dataclasses import dataclass

T = TypeVar("T")

class SupportsSub(Protocol[T]):
    def __sub__(self, other: T) -> T:
        ...

RangeT = TypeVar("RangeT", bound=SupportsSub[object])

@dataclass
class Range(Generic[RangeT]):
    start: RangeT
    end: RangeT
    def difference(self) -> RangeT:
        return self.end - self.start  # error: Incompatible return value type (got "object", expected "RangeT")
