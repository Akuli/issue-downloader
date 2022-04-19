from typing import TypeVar

T1 = TypeVar("T1")
T2 = TypeVar("T2")


def foo(a: T1, b: T2) -> T1 | T2:
    return a

invalid = 1 if 1 else foo(1, "s") # error: Argument 2 to "foo" has incompatible type "str"; expected "int"
valid = foo(1, "s") if 1 else 1
