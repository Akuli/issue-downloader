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
