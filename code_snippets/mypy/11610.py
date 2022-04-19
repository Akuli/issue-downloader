from typing import TypeVar, Callable, Iterable, Optional, List, Any

T = TypeVar("T")

def g(f: Callable[[T, T], T], seq: Iterable[Optional[T]]) -> Optional[T]: ...

a: List[Any]
# Incompatible types in assignment (expression has type "Optional[SupportsLessThanT]", variable has type "Optional[int]")
b: Optional[int] = g(min, a)  # Error!

a2: List[int]
b2: Optional[int] = g(min, a2)  # No error

