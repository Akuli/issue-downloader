from typing import NamedTuple, TypeVar, Generic
from typing_extensions import Protocol
from mypy_extensions import TypedDict

@xyz  # No error
class N1(NamedTuple):
   x: int

@xyz  # No error
class T1(TypedDict):
    x: int

class N2(NamedTuple, Protocol):  # No error
   x: int

class T2(TypedDict, Protocol):  # No error
    x: int

class M(type):
    def f(cls) -> None: pass

class N3(NamedTuple, metaclass=M):  # No error
   x: int

N3.f()  # Error

class T3(TypedDict, metaclass=M):  # No error
    x: int

T = TypeVar('T')

class N4(NamedTuple, Generic[T]):  # No error
   x: int

class T4(TypedDict, Generic[T]):  # No error
   x: int
