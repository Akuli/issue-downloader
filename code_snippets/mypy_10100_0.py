from typing import TypeVar, Any
T = TypeVar("T", bound=Any)

def this_one_works(x: T) -> T:
    res = x.__new__(type(x))
    return res
