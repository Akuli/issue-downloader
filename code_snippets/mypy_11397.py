from typing import overload


@overload
def foo(value1: str, value2: bool = False) -> str: # this default value is wrong/useless
    ...


@overload
def foo(value1: int, value2: bool = False) -> int: # this default value is wrong/useless
    ...


def foo(value1: str | int, value2: bool = True) -> str | int:
    ...
