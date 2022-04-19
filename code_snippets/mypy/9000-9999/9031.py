# mypy version 0.770
from typing import Generic, TypeVar

T = TypeVar("T", int, str)

class A:
  foo: int

class B(Generic[T]):
  foo: T

class C(B[int], A):
  pass

reveal_type(A().foo)
reveal_type(B().foo)
reveal_type(C().foo)
