from typing import Optional

def f() -> None:
    a = None
    while True:
        g(a)  # <-- No error here!
        a = [1]

def g(a: Optional[str]) -> None:
    pass
