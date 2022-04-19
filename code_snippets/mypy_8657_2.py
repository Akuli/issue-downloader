import enum

from typing import Literal

class _MissingType(enum.Enum):

    MISSING = enum.auto()

    def __repr__(self) -> str:
        return self.name

MISSING: Literal[_MissingType.MISSING] = _MissingType.MISSING
