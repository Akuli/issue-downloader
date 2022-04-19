from typing import TypeVar

T = TypeVar("T", int, str)


def foo() -> T:
    return 1 # error: Incompatible return value type (got "int", expected "str")  [return-value]

def bar() -> T:
    return "" # error: Incompatible return value type (got "str", expected "int")  [return-value]
