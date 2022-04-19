from typing import *

T = TypeVar('T')

@overload
def f1(x: int) -> int: ...
@overload
def f1(x: T) -> T: ...
def f1(*args, **kwargs): pass
