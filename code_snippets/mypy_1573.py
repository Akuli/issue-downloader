from itertools import groupby
from typing import Iterator, Iterable, TypeVar, Callable, Tuple, Any

X, Key = TypeVar('X'), TypeVar('Key')
def sorted_groupby(sequence: Iterable[X], key: Callable[[X], Key]) -> Iterator[Tuple[Key, Iterator[X]]]:
    return groupby(sorted(sequence, key=key), key=key)
