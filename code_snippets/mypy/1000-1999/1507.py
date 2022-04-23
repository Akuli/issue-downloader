from typing import TypeVar, Callable
S = TypeVar('S')
def apply(f: Callable[[int], S]) -> S: pass
def g(x: S) -> S: pass
y = apply(g) # E: Argument 1 to "apply" has incompatible type Callable[[S], S]; expected Callable[[int], S]
reveal_type(y) # E: Revealed type is 'S`-1'

tokenprog, pseudoprog, single3prog, double3prog = map(
    re.compile, (Token, PseudoToken, Single3, Double3))
