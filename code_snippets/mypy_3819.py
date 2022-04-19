from typing import *

@overload
def f(arg: str = "foo") -> AbstractSet[Tuple[str, str]]: ...

@overload
def f(arg: int = 0) -> AbstractSet[Tuple[str, Tuple[str, int]]]: ...
