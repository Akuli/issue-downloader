from collections import deque
from typing import Any, Callable, Generic, List, Protocol, TypeVar

T = TypeVar("T")

def test(item_type: T) -> None:
    a: deque[List[T]] = deque()
    b: deque[List[T]] = a.copy()  # ok


class Test(Generic[T]):
    def test(self) -> None:
        a: deque[List[T]] = deque()
        b: deque[List[T]] = a.copy()  # error: Incompatible types in assignment (expression has type "deque[List[List[T]]]", variable has type "deque[List[T]]")  [assignment]
