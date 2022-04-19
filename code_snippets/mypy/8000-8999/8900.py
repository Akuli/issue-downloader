from typing import Any, Callable, TypeVar, _T as T

def bar() -> None:
    def inner() -> None:
        it.encode()  # error: Cannot determine type of 'it'
    breaks()
    it = ""
    
deco: Callable[[T], T]

@deco
def breaks() -> None: ...

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

from typing import Any, TypeVar, _T as T

def bar() -> None:
    def inner() -> None:
        it.encode()  # no error
    doesnt_break()
    it = ""
    
def deco(fn: T) -> T: ...

@deco
def doesnt_break() -> None: ...
