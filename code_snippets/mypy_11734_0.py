from functools import singledispatch

@singledispatch
def f(x: object) -> int:
    return 1

@f.register
def _(x: int, y: str) -> int:
    return 2

print(f(1))  # No error reported, but fails at runtime
