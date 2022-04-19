from typing import TypeVar, Union


T = TypeVar("T")


def get_or_str(value: T) -> Union[str, T]:
    return value


def f(b: bool) -> Union[str, bool]:
    return "" if b else get_or_str(True)
