# test_cast.py
from operator import __gt__, __lt__
from typing import Callable, TypeVar, Union

_T = TypeVar("_T")

def identity(__: _T) -> _T:
    return __

maybe_not_available_decorator = identity  # <-- problematic decorator alias

# try:
#     from spicy import spicy_decorator as maybe_not_available_decorator
# except ImportError:
#     pass

class Spam:
    def __init__(self, value: int):
        super().__init__()
        self._value = value

    @identity  # <- function
    def __lt__(self, other: Union[int, "Spam"]) -> bool:  # <-- this is fine
        if isinstance(other, Spam):
            return __lt__(self._value, other._value)
        else:
            return NotImplemented

    @identity  # <- function
    def __gt__(self, other: Union[int, "Spam"]) -> bool:  # <-- so is this
        if isinstance(other, Spam):
            return __gt__(self._value, other._value)
        else:
            return NotImplemented

class Ham:
    def __init__(self, value: int):
        super().__init__()
        self._value = value

    @maybe_not_available_decorator  # <- alias
    def __lt__(self, other: Union[int, "Ham"]) -> bool:  # <-- Cannot determine type of "__gt__"
        if isinstance(other, Ham):
            return __lt__(self._value, other._value)
        else:
            return NotImplemented

    @maybe_not_available_decorator  # <- alias
    def __gt__(self, other: Union[int, "Ham"]) -> bool:  # <-- this is fine for some reason
        if isinstance(other, Ham):
            return __gt__(self._value, other._value)
        else:
            return NotImplemented
