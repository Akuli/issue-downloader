@overload
def open(mode: Literal["r"] = ...) -> int: ...
@overload
def open(mode: Literal["w"]) -> str: ...
@overload
def open(mode: str) -> str | int: ...

mode: str = ...
open(mode)
