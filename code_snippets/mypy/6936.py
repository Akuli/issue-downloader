from typing import cast, Generic, Optional, TypeVar, Union
from whereever import MustUse

T = TypeVar("T")
E = TypeVar("E")

# We inherit from MustUse to ensure this type isn't ignore
class Result(Generic[T, E], MustUse):
    def __init__(self, value: Union[T, E], is_ok: bool):
        self._value = value
        self.is_ok = is_ok

    @classmethod
    def ok(cls, value: T) -> "Result[T, E]":
        return cls(value, is_ok=True)

    @classmethod
    def error(cls, value: E) -> "Result[T, E]":
        return cls(value, is_ok=True)

    @property
    def is_error(self) -> bool:
        return not self.is_ok

    def get_value(self) -> Optional[T]:
        if self.is_ok:
            return cast(T, self._value)
        return None

    def get_error(self) -> Optional[E]:
        if not self.is_ok:
            return cast(E, self._value)
        return None

def f(success: bool) -> Result[str, int]:
    if not success:
        return Result[str, int].error(123)
    return Result[str, int].ok("Hello")


# No warning is raised since the value is saved to a variable
a = f(True)

# No warning is raised since we convert the Result into an Optional
f(False).get_value()

# This will raise a warning since we never do anything with the Result like:
#     error: unused return value with attribute MustUse
# or
#     error: return value of function call must be used
f(True)
