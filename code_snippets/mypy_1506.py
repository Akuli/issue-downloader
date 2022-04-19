from typing import TypeVar, Callable
S = TypeVar('S')
def apply(f: Callable[[int], S]) -> S: pass
def g(x: int) -> S: pass
y = apply(g)
reveal_type(y) # E: Revealed type is 'S`-1'
