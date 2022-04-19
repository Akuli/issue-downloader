from typing import Any

def f(x: Any) -> None:
    y = x
    y = 1
    reveal_type(y)  # Any
