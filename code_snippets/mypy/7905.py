from typing_extensions import Literal, TypedDict
from enum import Enum

class Key(Enum):
    X = 1
    Y = 2
    Z = 3

class MyDict(TypedDict):
    key: Literal[Key.X, Key.Y]
    blah: int

KEY: Literal["key"] = "key"

d: MyDict

if d["key"] is Key.X:
    reveal_type(d["key"])  # note: Revealed type is 'Literal[Key.X]'

if d[KEY] is Key.X:
    reveal_type(d[KEY])  # note: Revealed type is 'Literal[Key.X, Key.Y]'

