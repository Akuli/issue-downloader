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
