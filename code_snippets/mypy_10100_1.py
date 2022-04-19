from typing import TypeVar, Any
T = TypeVar("T", bound=Any)

def this_one_not_so_much(x: T) -> T:
    res = type(x).__new__(type(x))
    return res
