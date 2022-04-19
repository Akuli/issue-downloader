from dataclasses import dataclass
from typing import Generic, List, TypeVar


T = TypeVar('T', int, str)


@dataclass
class A(Generic[T]):
    x: List[T]


@dataclass
class B(A[int]):
    pass


B(x=[1])  # error: List item 0 has incompatible type "int"; expected "T"
