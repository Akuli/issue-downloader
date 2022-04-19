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


from typing import Generic, TypeVar
T = TypeVar("T", bound="A")

class A(Generic[T]):
    ...

class B(A["B"]):
    ...

class C(A["C"]):
    ...

def f(x: T, y: T) -> T:
    return x

b = B()
c = C()
res_typed: A = f(b, c) # OK
res_untyped = f(b, c) # mypy error
# type-var - Value of type variable "T" of "f" cannot be "object"


from typing import Generic, TypeVar
T = TypeVar("T", bound="D", covariant=True)

class A(Generic[T]):
    ...

class D(Generic[T]):
    ...

class E(D["E"]):
    ...

class F(D["F"]):
    ...

class B(A[E]):
    ...

class C(A[F]):
    ...

def f(x: A[T], y: A[T]) -> A[T]:
    return x

b = B()
c = C()
res_typed: A = f(b, c) # OK
res_typed2: A[D] = f(b, c) # OK
res_untyped = f(b, c) # mypy error
# type-var - Value of type variable "T" of "f" cannot be "object"


