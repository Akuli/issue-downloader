from typing import *

T = TypeVar('T')

@overload
def f1(x: int) -> int: ...
@overload
def f1(x: T) -> T: ...
def f1(*args, **kwargs): pass

class Wrapper(Generic[T]):
    @overload
    def f2(self, x: int) -> int: ...
    @overload
    def f2(self, x: T) -> T: ...
    def f2(self, *args, **kwargs): pass

class Dummy(Generic[T]): pass

@overload
def f3(d: Dummy[T], x: int) -> int: ...
@overload
def f3(d: Dummy[T], x: T) -> T: ...
def f3(*args, **kwargs): pass

