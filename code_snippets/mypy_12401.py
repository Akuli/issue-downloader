from typing import overload

@overload
def foo(a: int) -> int: ...

@overload
def foo(a: float) -> int: ...

def foo(a: object) -> object:  # no error
    return object()
