from typing import Any, Callable, TypeVar

T = TypeVar("T")

deco: Callable[[T], T]

@deco
def doesnt_break() -> None: ...

def bar() -> None:
    def inner() -> None:
        it.encode()  # no error
    doesnt_break()
    it = ""
