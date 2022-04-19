from typing import Generic, TypeVar
T = TypeVar("T", bound="A", covariant=True)

class A(Generic[T]):
    ...

class B(A["B"]):
    ...

class C(A["C"]):
    ...

def f(x: A[T], y: A[T]) -> A[T]:
    return x

b = B()
c = C()
res_typed: A = f(b, c) # OK
res_typed2: A[A] = f(b, c) # OK
res_untyped = f(b, c) # mypy error
# type-var - Value of type variable "T" of "f" cannot be "object"

