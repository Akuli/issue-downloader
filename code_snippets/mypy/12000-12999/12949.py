from typing import List

class IntList(List[int]):
    pass

T = TypeVar("T")

def f(s: List[T]) -> T:
    reveal_type(s)
    if isinstance(s, IntList):
        reveal_type(s)
        s.pop()
    reveal_type(s)
    return s.pop()
