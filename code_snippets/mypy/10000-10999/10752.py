from typing import Any, Callable, overload

@overload
def foo(a: Callable) -> int: ...
@overload
def foo(a: Any) -> Any: ...

def foo(a):
    pass

a: str = foo(lambda x: x)

from typing import Any, overload

@overload
def foo(a: int) -> int: ...
@overload
def foo(a: Any) -> Any: ...

def foo(a):
    pass

a: str = foo(1)
# mypy error: Incompatible types in assignment (expression has type "int", variable has type "str")

from typing import Any, Callable, overload

@overload
def foo(a: Callable) -> int: ...
@overload
def foo(a: int) -> Any: ...

def foo(a):
    pass

a: str = foo(lambda x: x)
# mypy error: Incompatible types in assignment (expression has type "int", variable has type "str")
