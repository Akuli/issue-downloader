from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    Point = tuple[int, int]  # mypy error: "tuple" is not subscriptable


def foo(p: Point) -> None:
    print(p)
