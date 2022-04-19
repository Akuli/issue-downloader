from typing import *
from dataclasses import dataclass
from abc import ABC, abstractmethod

T = TypeVar("T")

class Foo(ABC, Generic[T]):
    @abstractmethod
    def foo(self, other: T) -> T: ...

RangeT = TypeVar("RangeT", bound=Foo['RangeT'])

class Thing(Foo['Thing']):
    def foo(self, other: Thing) -> Thing: return self
    
@dataclass
class Range(Generic[RangeT]):
    start: RangeT
    end: RangeT
    def difference(self) -> RangeT:
        return self.end.foo(self.start)

a: Range[Thing] = Range(Thing(), Thing())
