from typing import Generic, Iterable, Iterator, Sequence, TypeVar
_T = TypeVar('_T')

class Windowed(Generic[_T]):
    def __init__(self, it: Iterable[_T], size: int) -> None:
        self.it = it
        self.size = size

    def __iter__(self) -> Iterator[Sequence[_T]]:
        iters = tee(self.it, self.size)
        slices = map(islice, iters, count(0), repeat(None))
        return zip(*slices)

def islice(iterable: Iterable[_T], start: Optional[int], stop: Optional[int],
           step: Optional[int] = ...) -> Iterator[_T]: ...

