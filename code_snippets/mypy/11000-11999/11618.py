def foo(x: Optional[dict] = None):
    if x is None:
        x = {}

from typing import Optional, TypeVar

T = TypeVar("T")


def assign_if_none(obj: Optional[T], assignment: T) -> T:

    return assignment if obj is None else obj

def foo(x: Optional[dict] = None):
    x = assign_to_none(x, {})

from typing import Mapping, Optional, TypeVar

T = TypeVar("T")


def assign_if_none(obj: Optional[T], assignment: T) -> T:

    return assignment if obj is None else obj


def func_1(mapping: Optional[dict] = None) -> str:

    mapping = assign_if_none(mapping, {})

    if "key" in mapping:
        return "Included"

    return "Excluded"


def func_2(mapping: Optional[Mapping[str, str]] = None) -> str:

    mapping = assign_if_none(mapping, {})

    if "key" in mapping:
        return "Included"

    return "Excluded"
