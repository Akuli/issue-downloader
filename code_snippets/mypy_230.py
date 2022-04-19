from typing import List, TypeVar
T = TypeVar('T')
def f(a: List[T], b: List[T]) -> None: pass
x = ['']
f(x, [])  # Cannot infer type argument 1 of "f"
