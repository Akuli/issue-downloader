from typing import TypeVar

_T = TypeVar('_T')
def foo(a: _T = 42) -> _T:  # E: Incompatible types in assignment (expression has type "int", variable has type "_T")
    return a
