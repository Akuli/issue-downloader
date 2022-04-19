# pair.py
from typing import Tuple, TypeVar

A = TypeVar('A')
B = TypeVar('B')

Pair = Tuple[A, B]

def fst(pair: Pair[A, B]) -> A:
    a, _ = pair
    return a

def snd(pair: Pair[A, B]) -> B:
    _, b = pair
    return b
