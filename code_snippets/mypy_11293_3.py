# test_case_import.py
from typing import Callable, TypeVar
_T = TypeVar("_T")

def _identity(__: _T) -> _T:
    return __

decr: Callable[[_T], _T] = _identity  # <-- doesn't matter how this is defined
