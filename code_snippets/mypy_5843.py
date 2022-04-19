from typing import Callable, Generic, TypeVar

_T = TypeVar('_T')
_U = TypeVar('_U')

class A(Generic[_T]):
    _value: _T
    def __init__(self, val: _T) -> None: ...
    def __rshift__(self, f: Callable[[_T], _U]) -> _U: ...

def inc(x: int) -> int: ...

A(1) >> inc  # No error
A(1).__rshift__(lambda x: x + 1)  # No error
A(1) >> (lambda x: x + 1)
#        │         └ Expression has type "Any"
#        └ Expression type contains "Any" (has type Callable[[Any], Any])
