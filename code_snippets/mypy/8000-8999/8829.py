from typing import Any, Optional, TypeVar

T = TypeVar("T")


def assert_not_none(value: Optional[T]) -> T:
    assert value is not None
    return value


def foo1(a: Optional[Any]) -> int:
    return assert_not_none(a)[3]


def foo2(a: Optional[Any]) -> int:
    assert a is not None
    return a[3]

