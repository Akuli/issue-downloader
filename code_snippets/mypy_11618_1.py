from typing import Optional, TypeVar

T = TypeVar("T")


def assign_if_none(obj: Optional[T], assignment: T) -> T:

    return assignment if obj is None else obj
