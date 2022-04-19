from typing import Type

def untyped_function():
    return int

def foo() -> Type[int]:
    x = untyped_function()
    assert issubclass(x, int)
    return x
