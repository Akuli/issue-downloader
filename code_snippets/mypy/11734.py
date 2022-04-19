from functools import singledispatch

@singledispatch
def f(x: object) -> int:
    return 1

@f.register
def _(x: int, y: str) -> int:
    return 2

print(f(1))  # No error reported, but fails at runtime

from functools import singledispatch

@singledispatch
def f(x: object, y: str) -> None:
    y + ''

@f.register
def _(x: int, y: int) -> None:
    y + 1

print(f(1, 'x'))  # No error reported, but fails at runtime

from functools import singledispatch

@singledispatch
def f(x: object, y: str) -> None:
    pass

@f.register
def _(x: int, yy: str) -> None:
    pass

print(f(1, y='x'))  # No error reported, but fails at runtime

