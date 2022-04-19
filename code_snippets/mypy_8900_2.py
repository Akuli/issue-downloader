from typing import Any, TypeVar, _T as T

def bar() -> None:
    def inner() -> None:
        it.encode()  # no error
    doesnt_break()
    it = ""
    
def deco(fn: T) -> T: ...

@deco
def doesnt_break() -> None: ...
