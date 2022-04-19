import csv
from typing import Callable, Iterable, Iterator, Text, TypeVar

T = TypeVar('T')

def foo(x: str, reader: Callable[[Iterable[Text]], Iterator[T]]) -> Iterator[T]:
    return reader(x)


# Is fine, resolves to Iterator[List[str]]
x = foo('bar.txt', csv.reader)


# Complains that _reader is not compatible with Iterator[T]
def baz(x: str, reader: Callable[[Iterable[Text]], Iterator[T]] = csv.reader) -> Iterator[T]:
    return reader(x)
