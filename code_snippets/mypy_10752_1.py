from typing import Any, overload

@overload
def foo(a: int) -> int: ...
@overload
def foo(a: Any) -> Any: ...

def foo(a):
    pass

a: str = foo(1)
# mypy error: Incompatible types in assignment (expression has type "int", variable has type "str")
