from dataclasses import dataclass
from typing import Final

@dataclass
class FirstClass:
    FIRST_CONST: Final = 3

@dataclass  # mypy runs fine if this isn't a dataclass
class SecondClass:
    SECOND_CONST: Final = FirstClass.FIRST_CONST
