from typing import Generic, TypeVar, generic_mro

T = TypeVar("T")
class A(Generic[T]): ...

U = TypeVar("U")
class B(A[U]): ...

class C(B[int]):
    pass

assert generic_mro(C) == (C, B[int], A[int], Generic, object)
assert generic_mro(B) == (B, A[U], Generic, object)
assert generic_mro(B[int]) == (B[int], A[int], Generic, object)
