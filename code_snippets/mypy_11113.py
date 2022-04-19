from typing import TypeVar

T = TypeVar("T", str, int)


def hi(value: T) -> None:
    value.asdfasdf  # error
    (qux := value.asdfasdf)  # no error
