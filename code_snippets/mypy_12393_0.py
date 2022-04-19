from typing import Callable, TypeAlias

A = Callable[[], str] | int  # error: Unsupported left operand type for | ("object")
B: TypeAlias = Callable[[], str] | int  # error: Unsupported left operand type for | ("object")
