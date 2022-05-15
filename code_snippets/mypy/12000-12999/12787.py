from enum import ReprEnum, Flag
class MyFlag(ReprEnum, Flag): ...

from enum import Enum, Flag
class ReprEnum(Enum): ...
class MyFlag(ReprEnum, Flag): ...

class ReprEnum(Enum):
    """
    Only changes the repr(), leaving str() and format() to the mixed-in type.
    """

# Much further down...

class IntFlag(int, ReprEnum, Flag, boundary=EJECT):
    """
    Support for integer-based Flags
    """
