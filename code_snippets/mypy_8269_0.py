from typing import Callable, Protocol

class F(Protocol):
    def __call__(self, *__args: str,  __arg: int) -> int: ...


def f(*__args: str, __arg: int) -> int: ...

f_: F = f
