import enum

from typing import Literal

class Color(enum.Enum):

    BLACK = enum.auto()

BLACK = Color.BLACK
BLACK_ALIAS: Literal[Color.BLACK] = Color.BLACK

reveal_type(Color.BLACK)
reveal_type(BLACK)
reveal_type(BLACK_ALIAS)

import enum

from typing import Literal, Optional

class Color(enum.Enum):

    BLACK = enum.auto()

BLACK = Color.BLACK
BLACK_ALIAS: Literal[Color.BLACK] = Color.BLACK

x: Optional[Literal[Color.BLACK]] = None
y: Optional[Literal[BLACK]] = None
z: Optional[Literal[BLACK_ALIAS]] = None

reveal_type(x)
reveal_type(y)
reveal_type(z)

import enum

from typing import Literal

class _MissingType(enum.Enum):

    MISSING = enum.auto()

    def __repr__(self) -> str:
        return self.name

MISSING: Literal[_MissingType.MISSING] = _MissingType.MISSING

MissingLiteral = Literal[_MissingType.MISSING]

x: Optional[MissingLiteral] = None

