from typing import *
from dataclasses import dataclass

T = TypeVar("T")

class SupportsSub(Protocol[T]):
    def __sub__(self, other: T) -> T: ...

RangeT = TypeVar("RangeT", bound=SupportsSub[Any])
    
@dataclass
class Range(Generic[RangeT]):
    start: RangeT
    end: RangeT
    def difference(self) -> RangeT:
        return cast(RangeT, self.end - self.start)

a: Range[int] = Range(1, 2)
