from __future__ import annotations
from typing import TypeVar, Union
import numpy

T = TypeVar("T")

def _test(a: list[T]) -> Union[numpy.ndarray, T]:
    if isinstance(a[0], str):
        return a[0]
    return numpy.array(a)
