from typing import Any

x = 'a'
y: Any = 1

lst = [x, y]
lst[0] >> 1  # not detected by mypy, fails at runtime, will be fixed by rule (3)

def f(x: int) -> None:
    x >> 1
def g(x: Any) -> None:
    pass

funs = [f, g]
funs[0]('a')  # not detected by mypy, fails at runtime, will be fixed by rule (4)
