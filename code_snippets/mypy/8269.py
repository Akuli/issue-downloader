from typing import Callable, Protocol

class F(Protocol):
    def __call__(self, *__args: str,  __arg: int) -> int: ...


def f(*__args: str, __arg: int) -> int: ...

f_: F = f

class G(Protocol):
    def __call__(self, __arg: int, *__args: str) -> int: ...
    
def g(__arg: int, *__args: str) -> int: ...
g_: G = g
