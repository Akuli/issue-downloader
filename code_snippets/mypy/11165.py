from typing import (
        Literal,
        overload,
        Sequence,
        TypeVar,
        Union,
        )

T1 = TypeVar('T1')
T2 = TypeVar('T2')

@overload
def func(a1: Literal[True], a2: T1) -> Union[T1, Sequence[T2]]: ...
    # error: Overloaded function signatures 1 and 2 overlap with incompatible return types  [misc]

@overload
def func(a1: bool, a2: T1) -> Union[T1, Sequence[T2], T2]: ...

def func(  # type: ignore[misc]  # bug #11159
        a1: bool, a2: T1) -> Union[T1, Sequence[T2], T2]:
    pass
