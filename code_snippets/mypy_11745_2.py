# main.py

from __future__ import annotations
from typing import Any, TypeVar              


class SupportsIAdd:          
    def __iadd__(self, other: Any) -> SupportsIAdd: ...         


class AddingAccumulatorParam:            
    def addInPlace(self, value1: SupportsIAdd, value2: SupportsIAdd) -> SupportsIAdd:            
        value1 += value2
        return value1
