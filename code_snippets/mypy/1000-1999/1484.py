from typing import *
from functools import partial

def inc(a:int) -> int:
    return a+1

def foo(f: Callable[[], int]) -> int:
    return f()

foo(partial(inc, 1))
