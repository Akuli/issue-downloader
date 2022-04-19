import contextlib
from typing import Iterator

@contextlib.contextmanager
def f() -> Iterator[int]:
    return iter([1])


with f():
    pass


with f():
    raise TypeError('wat')
