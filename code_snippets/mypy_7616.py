from typing import Iterable, Iterator, Union
from typing_extensions import Protocol

class MixedIter(Protocol):
    def __iter__(self) -> Iterator[Union[int, str]]: ...

def f(xs: Iterable[Union[int, str]]) -> str:
    return ''.join(str(x) for x in xs)

def g(xs: MixedIter) -> str:
    return ''.join(str(x) for x in xs)

mixedTuple = (56, 'A')
reveal_type(mixedTuple)
reveal_type(mixedTuple.__iter__)
print(f(mixedTuple))
print(g(mixedTuple))
