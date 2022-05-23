from collections.abc import Mapping
from typing import TypeVar

T = TypeVar("T")
S = TypeVar("S")

def swap(x: Mapping[T, S]) -> Mapping[S, T]:
    if isinstance(x, dict):
        return x
    else:
        raise Exception
