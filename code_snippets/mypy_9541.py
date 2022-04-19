from typing import Optional

def func(x: Optional[int]) -> int:
    if isinstance(x, type(None)):
        return 0
    else:
        return x + 1  # This is line 7
