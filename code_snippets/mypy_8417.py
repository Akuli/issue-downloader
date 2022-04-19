import attr
from typing import Sequence

@attr.s(auto_attribs=True)
class Foo:
    things: Sequence[str]

@attr.s(auto_attribs=True)
class Bar:
    things: Sequence[str] = attr.ib(converter=tuple)

@attr.s(auto_attribs=True)
class Raz:
    thing: str = attr.ib(converter=str) 

Foo(['hello', 'world'])
Raz('hello')
Bar(['hello', 'world'])
reveal_type(Foo.__init__)
reveal_type(Bar.__init__)
reveal_type(Raz.__init__)
