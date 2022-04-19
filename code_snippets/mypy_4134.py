from typing import AnyStr
def f(x: AnyStr) -> bytes:
    return x.encode("ascii") if isinstance(x, str) else x
