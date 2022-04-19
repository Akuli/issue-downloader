# poc.py
from dataclasses import dataclass
from typing import Protocol, Final

@dataclass
class FinalY:
    y: Final[int] = 0

class Y(Protocol):
    y: int

def f(x: Y) -> Y:
    x.y = 42
    return x

print(f(FinalY(17)))
