from typing import Tuple, TypeVar

A = TypeVar('A')
B = TypeVar('B')

class Pair(Tuple[A, B]):

    def fst(pair: Pair[A, B]) -> A:
        a, _ = pair
        return a

    def snd(pair: Pair[A, B]) -> B:
        _, b = pair
        return b


def f(pair: Pair[int, float]) -> float:
    return Pair.fst(pair) + Pair.snd(pair)

pair: Pair[int, float] = (1, 1.5)
assert f(pair) == 2.5
