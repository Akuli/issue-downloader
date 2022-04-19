from functools import singledispatch

@singledispatch
def f(x: object, y: str) -> None:
    y + ''

@f.register
def _(x: int, y: int) -> None:
    y + 1

print(f(1, 'x'))  # No error reported, but fails at runtime
