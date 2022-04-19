from typing import *
from dataclasses import dataclass

T = TypeVar("T")

class SupportsSub(Protocol[T]):
    def __sub__(self, other: T) -> T: ...

@dataclass
class Range(Generic[T]):
    start: T
    end: SupportsSub[T]
    def difference(self) -> T:
        return self.end - self.start

a: Range[int] = Range(1, 2)
