from typing import Optional, Callable

def f1(key: Callable[[], str]) -> None: ...
def f2(key: object) -> None: ...

def g(b: Optional[str]) -> None:
    if b:
        f1(lambda: b.upper())  # Item "None" of "Optional[str]" has no attribute "upper"
        z: Callable[[], str] = lambda: b.upper()  # Item "None" of "Optional[str]" has no attribute "upper"
        f2(lambda: b.upper())  # No error
        lambda: b.upper()  # No error
