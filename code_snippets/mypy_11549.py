from __future__ import annotations
from typing import Generic, TypeVar, ClassVar, Any

T = TypeVar("T")


class A(Generic[T]):
    @classmethod
    def bar(cls: type[A[int]]) -> None:
        ...


A.bar()  # error: Invalid self argument "Type[A[Any]]" to attribute function "bar" with type "Callable[[Type[A[int]]], None]"
A_Alias1 = A
A_Alias1.bar()  # error: Invalid self argument "Type[A[Any]]" to attribute function "bar" with type "Callable[[Type[A[int]]], None]"
reveal_type(A_Alias1)  # note: Revealed type is "def [T] () -> __main__.A[T`1]"

A_Alias2 = A[Any]
A_Alias2.bar()  # valid
reveal_type(A_Alias2)  # note: Revealed type is "def () -> __main__.A[Any]"


def foo(a: type[A[int]]) -> None:
    ...
    
foo(A)  # no error
foo(A_Alias1)  # error: Argument 1 to "foo" has incompatible type "Type[A[Any]]"; expected "Type[A[int]]"

