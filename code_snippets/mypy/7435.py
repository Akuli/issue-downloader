from typing_extensions import Literal, TypedDict
from typing import Optional

class Super:
    type: str

class Foo(Super):
    type: Literal['foo']

class SuperDict(TypedDict):
    type: str

class Bar(SuperDict):
    type: Literal['bar']

class SuperTuple(NamedTuple):
    type: str

class Baz(SuperTuple):
    type: Literal['baz']
