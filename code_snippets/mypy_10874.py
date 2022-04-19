@dataclass
class Range:
    start: object
    end: object
    def difference(self):
        return self.end - self.start

a = Range(1, 2)

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

T = TypeVar("T")

class SupportsSub(Protocol[T]):
    def __sub__(self: T, other: T) -> T:
        ...

class Fake:
    def __sub__(self, other: int) -> int: return 21
    
a: SupportsSub[int] = Fake()

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

