from typing import Optional


def test_something(x: Optional[str] = None, y: Optional[str] = None) -> str:
    if not (x or y):
        return "early"

    other: str = x or y  # <<< mypy complains that other should be Optional[str]

    return other

#!/usr/bin/env python3

from typing import Optional


def test_something(x: Optional[str] = None, y: Optional[str] = None) -> str:
    if not (x or y):
        return "early"

    other: str = x or y

    print(f"x = {x}")
    print(f"y = {y}")
    print(f"other class: {type(other)}")
    print()

    return other

test_something()
test_something(x="hello")
test_something(y="goodbye")
test_something(x="hello", y="goodbye")

strict = true
pretty = true
show_column_numbers = true
show_error_codes = true
show_error_context = true
