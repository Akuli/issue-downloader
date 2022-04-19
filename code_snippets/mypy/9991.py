from typing import *

x: Optional[int] = None
y: Optional[int] = None

def f() -> None:
    x = 1
    y = 1
    class C:
        reveal_type(x)  # Correctly reveals int
        reveal_type(y)  # Incorrectly reveals int, should be Optional[int]
        x = 2
