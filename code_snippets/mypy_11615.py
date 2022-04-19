from collections.abc import Collection, Mapping

def f(x: int | Collection[int] | Mapping[str, int]) -> int:
    r"""Recursively sum up all the values of possibly nested data."""
    if isinstance(x, int):
        return x
    if isinstance(x, Mapping):
        return sum(f(y) for y in x.values())

    reveal_type(x)   # <- Here, mypy thinks this is Collection only!

    if isinstance(x, Collection):
        reveal_type(x)  # <- Suddenly mypy thinks this is Collection | Mapping
        return sum(f(y) for y in x)
    raise TypeError(f"unsupported type: {type(x)}")
