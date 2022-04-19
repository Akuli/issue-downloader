from typing import MutableSet, Sequence, TypeVar

T = TypeVar('T', str, Sequence[str])

class CustomSet(MutableSet[T]):
    def add(self, value: T) -> None:
        pass

foo = CustomSet()
foo.add(('a', 'b'))
