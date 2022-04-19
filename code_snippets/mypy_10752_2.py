from typing import Any, Callable, overload

@overload
def foo(a: Callable) -> int: ...
@overload
def foo(a: int) -> Any: ...

def foo(a):
    pass

a: str = foo(lambda x: x)
# mypy error: Incompatible types in assignment (expression has type "int", variable has type "str")
