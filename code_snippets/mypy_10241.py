from typing import Optional, TypeVar

T1 = TypeVar("T1")
def func1(suffix: Optional[T1] = ...) -> T1:
    ...

T2 = TypeVar("T2", bound=str)
def func2(suffix: Optional[T2] = ...) -> T2:
    ...

T3 = TypeVar("T3", str, bytes)
def func3(suffix: Optional[T3] = ...) -> T3:
    ...

T4 = TypeVar("T4", bytes, str)
def func4(suffix: Optional[T4] = ...) -> T4:
    ...

reveal_type(func1()) # <nothing>
reveal_type(func2()) # <nothing>
reveal_type(func3()) # str
reveal_type(func4()) # bytes

from tempfile import mkstemp
_, temp_path = mkstemp()
reveal_type(temp_path) # str?

