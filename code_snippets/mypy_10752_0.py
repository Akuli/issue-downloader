from typing import Any, Callable, overload

@overload
def foo(a: Callable) -> int: ...
@overload
def foo(a: Any) -> Any: ...

def foo(a):
    pass

a: str = foo(lambda x: x)
