from typing import Optional

def the_method(maybe_int: Optional[int]):
    can_divide = bool(maybe_int)
    if can_divide:
        100 / maybe_int
