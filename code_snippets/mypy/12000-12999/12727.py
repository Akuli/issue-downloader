from typing import overload, Callable

@overload
def f() -> None: ...
@overload
def f(fn: Callable[[], object]) -> None: ...

def f(fn: object=1) -> None: ...

x: object
assert isinstance(x, str)
y = x
f(lambda: reveal_type(x))  # Revealed type is "str", Revealed type is "object"
f(lambda: reveal_type(y))  # Revealed type is "str"
