def my_sorted(__iterable: Iterable[_T], *, key: Callable[[_T], SupportsLessThan], reverse: bool = ...) -> List[_T]: ...

from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


def unwrap(val: T | None) -> T:
    assert val is not None
    return val


x: list[str | None]
sorted(x, key=lambda x: unwrap(x).upper())
#                       <nothing> has no attribute "upper"  [attr-defined]

