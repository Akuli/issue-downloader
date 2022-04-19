class C:
    x: int

    __hash__ = object.__hash__

from typing import NamedTuple

class C(NamedTuple):
    x: int

    __hash__ = object.__hash__

# mypy is ok with this
from typing import NamedTuple

class C(NamedTuple):
    x: int

    def __hash__(self) -> int:
        return object.__hash__(self)

