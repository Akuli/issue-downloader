from enum import IntEnum
from typing import Final, Type

class Colour(IntEnum):
    value: int
    r: Final[int]
    g: Final[int]
    b: Final[int]

    RED = 0, b"\xFF\x00\x00"
    GREEN = 1, b"\x00\xFF\x00"
    BLUE = 2, b"\x00\x00\xFF"
    
    def __new__(cls: Type["Colour"], value: int, _hue: bytes) -> "Colour":
        member = int.__new__(cls, value)
        member._value_ = value
        return member
      
    def __init__(self: "Colour", _value: int, hue: bytes) -> None:
        self.r = hue[0]
        self.g = hue[1]
        self.b = hue[2]
        
c = Colour(0)
print(c)
