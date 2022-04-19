from mypy_extensions import TypedDict
from typing import TypeVar, Generic, Type

T = TypeVar('T')

class G(Generic[T]):
    def __init__(self, x : Type[T]):
        self.x = x

D = TypedDict('D', {})

def f(x: G[D]):
    pass

f(G(D))
