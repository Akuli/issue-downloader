from __future__ import annotations
from typing import Any

def passes() -> tuple[str]:
    a: Any
    return (a,)

def fails_1() -> tuple[str]:
    a: int
    return (a,)
    # error: Incompatible return value type (got "Tuple[int]", expected "Tuple[str]")

def fails_2() -> str:
    a: Any
    return a
    # error: Returning Any from function declared to return "str"
