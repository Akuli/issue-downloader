from __future__ import annotations
from phantom.sized import NonEmpty, Empty

i: tuple[int, ...] = ()

assert isinstance(i, Empty)
assert isinstance(i, NonEmpty)

reveal_type(i)

class NonEmpty:
    ...

class Empty(Not[NonEmpty]):
    ...
