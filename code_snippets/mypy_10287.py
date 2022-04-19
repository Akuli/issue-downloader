# mypy: warn_unreachable
from typing import Generic, TypeVar, Union

T = TypeVar("T")
class A(Generic[T]): pass
class B(Generic[T]): pass
AorB = Union[A[T], B[T]]

x: AorB

if isinstance(x, A):
    print("A")
elif isinstance(x, B):
    print("B")
else:
    # correctly identified as unreachable
    reveal_type(x)
    print("not possible!")

y: AorB[int]

if isinstance(y, A):
    print("A")
elif isinstance(y, B):
    print("B")
else:
    # NOT identified as unreachable, although it should be
    reveal_type(y)
    print("not possible!")

