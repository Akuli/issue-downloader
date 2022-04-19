from typing import Iterable, Iterator, Tuple, TypeVar

T = TypeVar('T')
S = TypeVar('S')

class C(Iterable[Tuple[T, S]]):
    def __iter__(self) -> Iterator[Tuple[T, S]]: pass

def f(*x: T) -> T: pass

x: C[str, int]
y: C[int, int]
reveal_type(f(*x))  # str, should be Tuple[str, int]
reveal_type(f(*y))  # int, should be Tuple[int, int]
