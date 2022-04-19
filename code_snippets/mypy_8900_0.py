from typing import Any, Callable, TypeVar, _T as T

def bar() -> None:
    def inner() -> None:
        it.encode()  # error: Cannot determine type of 'it'
    breaks()
    it = ""
    
deco: Callable[[T], T]

@deco
def breaks() -> None: ...
