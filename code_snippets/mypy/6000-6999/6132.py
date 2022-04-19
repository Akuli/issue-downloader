import typing
T = typing.TypeVar('T')
def same(obj: T) -> T:
    return obj
add = same(3).__add__
TypeVar = same(typing).TypeVar

[mypy]
disallow_untyped_defs = True

