from typing import Literal

a: Literal[1, 2, 3] = 2
assert a in (1, 2)
b: Literal[1, 2] = a
