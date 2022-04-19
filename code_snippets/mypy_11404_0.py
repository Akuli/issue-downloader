from typing import Optional


def test_something(x: Optional[str] = None, y: Optional[str] = None) -> str:
    if not (x or y):
        return "early"

    other: str = x or y  # <<< mypy complains that other should be Optional[str]

    return other
