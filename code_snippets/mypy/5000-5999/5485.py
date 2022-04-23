from dataclasses import dataclass
from typing import Callable

@dataclass
class Repro:
    fn: Callable[[int], str]

r = Repro(fn=repr)
assert "1" == r.fn(1)

class Repro:
    def __init__(self, fn: Callable[[int], str]) -> None:
        self.fn = fn
