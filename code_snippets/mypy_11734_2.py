from functools import singledispatch

@singledispatch
def f(x: object, y: str) -> None:
    pass

@f.register
def _(x: int, yy: str) -> None:
    pass

print(f(1, y='x'))  # No error reported, but fails at runtime
