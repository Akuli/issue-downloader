from typing import Generic, TypeVar, get_type_hints

T = TypeVar("T")
class A(Generic[T]):
    a: T

U = TypeVar("U")
class B(A[U]):
    b: U

assert get_type_hints(B) == {"a": T, "b": U}

assert get_type_hints(B, substitute_type_vars=True) == {"a": U, "b": U}  # typevars are consistent
assert get_type_hints(B[T], substitute_type_vars=True) == {"a": T, "b": T}
assert get_type_hints(B[int], substitute_type_vars=True) == {"a": int, "b": int}  # ready to use
