from typing import TypeVar, Generic, Union, Any

T = TypeVar('T')
Tcov = TypeVar('Tcov', covariant=True)
S = TypeVar('S')

class A(Generic[Tcov]): pass

class B(A[T]):
    def __add__(self, x: B[S]) -> B[Union[T, S]]: ...

a: A[object]
b1: B[Any]
b2: B[int]

a = b1 + b2  # Unsupported operand types for + ("B[Any]" and "B[int]")
