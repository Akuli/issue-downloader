from typing import Callable, TypeAlias

A = Callable[[], str] | int  # error: Unsupported left operand type for | ("object")
B: TypeAlias = Callable[[], str] | int  # error: Unsupported left operand type for | ("object")

C = int | Callable[[], str]  # No error using Python 3.10 (in a `.py file), or in a stub file on any Python version.

D = list[Callable[[], str] | int]

X = int | Callable[[], str | bool]  # error: Unsupported left operand type for | ("Type[str]")
Y = int | Callable[[str | bool], str]  # error: Unsupported left operand type for | ("Type[str]")
