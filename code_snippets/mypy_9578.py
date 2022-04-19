from typing import List, TypeVar
import attr

_Foo = TypeVar('_Foo', bound='Foo')  # comment this line and the problem goes away

@attr.s
class Foo:
    _type = List[str]
    bar = attr.ib(type=_type)
