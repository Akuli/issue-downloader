from typing import Callable, TypeVar, Union, overload

T = TypeVar('T')
U = TypeVar('U')

@overload
def call(*, f: Callable[[], T]) -> T: ...

@overload
def call(*, u: U) -> U: ...

def call(*, f: Callable[[], T] = None, u: U = None) -> Union[T, U, None]:
    return f() if f else u

def call(*, f: None = None, u: U) -> U: ...
