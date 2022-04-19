import enum

from typing import Literal

class Color(enum.Enum):

    BLACK = enum.auto()

BLACK = Color.BLACK
BLACK_ALIAS: Literal[Color.BLACK] = Color.BLACK

reveal_type(Color.BLACK)
reveal_type(BLACK)
reveal_type(BLACK_ALIAS)
