# test.py
from pair import Pair

def f(pair: Pair[int, float]) -> float:
    return Pair.fst(pair) + Pair.snd(pair)

pair: Pair[int, float] = (1, 1.5)
assert f(pair) == 2.5
