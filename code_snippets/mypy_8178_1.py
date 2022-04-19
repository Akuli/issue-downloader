from typing import NamedTuple

class Example(NamedTuple):
    a: int = 1
    b: int = 2
    # c: int = a*b
    d: int = does_not_exist*5
