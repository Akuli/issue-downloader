from typing import TypeVar

T = TypeVar("T")

def assert_something(expected: T, actual: T) -> None:
    ...

assert_something(1, "")  # no error, SUS alert!, T is inferred as `object`
