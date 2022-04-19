# test.py
import pair
from pair import Pair

def f(p: Pair[int, float]) -> float:
    return pair.fst(p) + pair.snd(p)

p: Pair[int, float] = (1, 1.5)
assert f(p) == 2.5
