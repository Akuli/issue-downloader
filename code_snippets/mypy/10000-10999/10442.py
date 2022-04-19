from __future__ import annotations

from typing import Any, Iterator

l_int: list[int] = [1, 2]

l_str: list[str]
l_str = ["a", "b"]

l_union: list[str] | list[bytes]
l_union = ["a", "b"]


def iter_yield() -> Iterator[list[Any]]:
    yield l_int
    yield l_str  # this passes


def iter_yield_from() -> Iterator[list[Any]]:
    reveal_type(l_int)  # builtins.list[builtins.int]
    reveal_type(l_str)  # builtins.list[builtins.str]
    reveal_type(l_union)  # Union[builtins.list[builtins.str], builtins.list[builtins.bytes]]

    yield from (
        l_int,
        l_str,
    )  # error: Incompatible types in "yield from" (actual type "object", expected type "List[Any]")

    yield from (
        l_int,
        l_str,
        l_union,
    )  # error: Incompatible types in "yield from" (actual type "object", expected type "List[Any]")

    yield from (
        l_int,
        l_union,
        l_str,
    )  # union on first or second position passes 🙃

# setup.cfg
[mypy]
python_version = 3.8
strict = true
warn_unreachable = true
implicit_reexport = true
ignore_missing_imports = true

