def identity(x: int) -> int:
    return x

def double(x: int) -> int:
    return x * 2

def add(x: int, y: int) -> int:
    return x + y

calls_same_signatures = (
    (identity, (1,)),
    (double, (2,)),
)

calls_different_signatures = (
    (identity, (1,)),
    (add, (1, 2)),
)

for f1, args1 in calls_same_signatures:
    f1(*args1) # type checks

for f2, args2 in calls_different_signatures:
    f2(*args2) # mypy says: Cannot call function of unknown type

from typing import Callable, Sequence, Tuple

def identity(x: int) -> int:
    return x

def double(x: int) -> int:
    return x * 2

def add(x: int, y: int) -> int:
    return x + y

calls_same_signatures: Sequence[Tuple[Callable[..., int], Tuple[int, ...]]]
calls_same_signatures = (
    (identity, (1,)),
    (double, (2,)),
)

calls_different_signatures: Sequence[Tuple[Callable[..., int], Tuple[int, ...]]]
calls_different_signatures = (
    (identity, (1,)),
    (add, (1, 2)),
)

f1: Callable[..., int]
for f1, args1 in calls_same_signatures: # type checks
    f1(*args1)

f2: Callable[..., int]
for f2, args2 in calls_different_signatures:  # mypy says: Incompatible types in assignment (expression has type "function", variable has type "Callable[..., int]")
    f2(*args2)
